import os, json, random, string
from langchain_groq import ChatGroq 
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.types import Command
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from src.supervisor_graph import SupervisorState
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant")

def churn_score_node(state:SupervisorState)->SupervisorState:
    """
        Calculate a churn risk score from user input.
        Returns category: high, medium, or low.
    """
    user_input=state['user_input']
    current_profile = state.get('customer_profile',{})
    system_prompt = """ 
    You are a churn detection assistant.
    Based on the user input, classifiy their churn risk into:
    - high: user explicitly wants to cancel, switch, or sounds very frustrated.
    - medium: user shows dissatisfaction but hasn't decided to cancel yet.
    - low: user just asking questions or mild complaints.

    Examples:
    User: "I'm cancelling this useless service today."
    Churn risk: high

    User: "Your prices keep going up, I don't know if it's worth it anymore."
    Churn risk: medium

    User: "How do I cancel if I ever need to in the future?"
    Churn risk: low

    Respond with only one of: high, medium, low.
    """
    score = llm.invoke([
        {'role':'system', 'content':system_prompt},
        {'role':'user', 'content':user_input}
    ]).content
    
    current_profile['churn_score']=score
    return {"customer_profile":current_profile}

def loyalty_score_node(state:SupervisorState)->SupervisorState:
    """ 
        Provide loyalty score to user based on churn score and customer value. 
    """
    score = state['customer_profile']['churn_score']
    current_profile = state.get('customer_profile')
    reward_weights = {'high': 1.0, "medium": 0.6, "low": 0.2}
    clv_values = {"high": 1000, "medium": 500, "low": 200}
    clv_tier=random.choices(
        ['high','medium','low'],
        weights=[0.25,0.45,0.3],
        k=1
        )[0]

    loyalty_score = reward_weights[score]*clv_values[clv_tier]
    current_profile['loyalty_score']=loyalty_score
    current_profile['clv_tier']=clv_tier

    return {'customer_profile':current_profile}

def reward_node(state:SupervisorState)->SupervisorState:
    """
    Generate a personalized reward offers.
    """

    user_input=state['user_input']
    churn_score=state['customer_profile']['churn_score']
    loyalty_score=state['customer_profile']['loyalty_score']

    system_prompt=""" 
    You are a customer retention assistant. 
    Generate a polite, empathetic message based on the following:
    - The user's message
    - Their churn risk (high, medium, low)
    - Their loyalty score (40-1000)

    Rules:
    - If loyalty score >= 800 → emphasize strong appreciation and give a high reward (e.g., big discount, free premium month).
    - If 500-799 → show gratitude and offer a medium reward (e.g., discount or perk).
    - If 200-499 → acknowledge their value and give a small reward (e.g., loyalty points or small discount).
    - If < 200 → do not give a reward, just apologize and promise to improve.
    - If churn risk = high → always start by apologizing and showing empathy before mentioning any reward.
    - Keep the message short, friendly, concise and natural. Do not include technical terms or scores.
    
    Respond with only the final concise message.
    """

    user_context = f"""
        User message: {user_input}
        Churn risk: {churn_score}
        Loyalty score: {loyalty_score}
        """

    response = llm.invoke([{'role':'system', 'content':system_prompt},
                           {'role':'user','content':user_context}])
    
    return {"messages":response.content}

def build_retention_graph():

    graph = StateGraph(SupervisorState)

    graph.add_node("churn_score",churn_score_node)
    graph.add_node("evaluate_user_value",loyalty_score_node)
    graph.add_node("offer_reward",reward_node)

    graph.add_edge(START, "churn_score")
    graph.add_edge("churn_score", "evaluate_user_value")
    graph.add_edge("evaluate_user_value", "offer_reward")
    graph.add_edge("offer_reward", END)
    memory=MemorySaver()
    return graph.compile(checkpointer=memory)

retention_graph = build_retention_graph()

def retention_flow(state:SupervisorState)->SupervisorState:
    config= {"configurable":{"thread_id":"user_complaint_session", "recursion_limit":5}}
    return retention_graph.invoke(state, config=config)