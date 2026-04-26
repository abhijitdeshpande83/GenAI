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

def rag_node(state:SupervisorState)->SupervisorState:
    "Answers general user inquiries that fall outside the automated support ticket workflow."
    user_input=state.get("user_input",[])

    system_prompt="""
        You are a helpful support assistant. Provide clear, concise answers to the user's questions.
        """
    response = llm.invoke([SystemMessage(system_prompt)]+[HumanMessage(user_input)])
    
    return {'messages':[response.content], "active_flow": None, "extracted_info":None}


def build_inquiry_node():
    graph = StateGraph(SupervisorState)
    
    graph.add_node("inquiry", rag_node)

    graph.add_edge(START, "inquiry")
    graph.add_edge("inquiry", END)

    return graph.compile()

inquiry_graph = build_inquiry_node()

def inquiry_flow(state:SupervisorState)->SupervisorState:
    
    return inquiry_graph.invoke(state)
