import os, json, random, string
from langchain_groq import ChatGroq 
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.types import Command
from langchain_core.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv
from src.supervisor_graph import SupervisorState
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant")

def greeting_flow(state:SupervisorState)->dict:

    """Greets the user warmly and sets the empathetic tone for the interaction."""
    
    user_input = state.get("user_input",[])
    prompt = f"""
    You are a helpful and empathetic Customer Success Assistant.
    Greet the user warmly based on their input: "{user_input}".
    """
<<<<<<< HEAD
    response = llm.invoke([SystemMessage(content=prompt)])
    
    return {"messages": [response.content], "active_flow": None}
=======
    res = llm.invoke([SystemMessage(content=prompt)])
    print(res)
    
    return {"messages": [res.content]}
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)

def clarification_flow(state: SupervisorState) -> dict:
    """Refines vague input into a specific intent (Complaint, Retention, or Inquiry)."""
    
    user_input = state.get("user_input", "")
    
    system_prompt = """
    Role: Support Triage Agent
    Context: The user's input is too vague to route to a specific workflow.
    
    Task: Acknowledge the user's message and ask a single, polite question to clarify if they:
    - Have a technical problem/defect (Complaint)
    - Want to cancel, return, or switch services (Retention)
    - Need general info or instructions (Inquiry)
    
    Constraint: Be empathetic but direct. Maximum 25 words.
    """
    
    # Invoking the LLM with the specific user input
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ])
    
    # Returning the response to update the message state
<<<<<<< HEAD
    return {"messages": [response.content], "active_flow": None}
=======
    return {"messages": [response.content]}
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)
