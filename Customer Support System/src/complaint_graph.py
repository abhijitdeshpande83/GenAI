import os, json, random, string
from typing import Annotated, Dict
from operator import add
from langchain_groq import ChatGroq 
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.types import Command
from langchain_core.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv
from src.supervisor_graph import SupervisorState
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant")

def extract_info_node(state:SupervisorState)->SupervisorState:
    """ 
    Extracts product, issue, and date from input into JSON.
    """
    user_input = state.get("user_input",[])

    system_prompt=f""" You are an entity extractor. 
    Your goal is to extract the product information, issue_type, and purchase_date 
    from the user's input.
    - product
    - issue_type
    - purchase_date

    Respond ONLY with a valid JSON object in this exact format:
    {{
        "product": string or null,
        "issue_type": string or null,
        "purchase_date": MM/DD/YY or null
    }}
    """
     
    res = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ])
    
    complaint_data = json.loads(res.content)
     
    return {"complaint_data":complaint_data}

def create_ticket_node(state:SupervisorState)->SupervisorState:
    """
    Finalizes the complaint by validating entity specificity and generating a user confirmation number.
    """
    complaint_data = state.get("complaint_data",[])
    
    prefix = ''.join(random.choices(string.ascii_uppercase,k=2))
    number1 = random.randint(100,1000)
    mid = ''.join(random.choices(string.ascii_uppercase))
    number2 = random.randint(10,100)
    ticket_id = f"{prefix}{number1}{mid}{number2}"

    ticket={
        "ticket_id":ticket_id,
        "status":"created",
        "details":complaint_data
    }
    return {"messages":f"Ticket {ticket['ticket_id']} has been created.", "active_flow": None}

def ask_missing_node(state:SupervisorState)->SupervisorState:
    """ 
    Prompts the user for specific missing details to complete the support ticket data.
    """
    
    complaint = state.get("complaint_data", {})
    missing_info = state.get("missing_info",{})
    prompt = f"The user provided: {complaint}. Politely ask for the following missing information {missing_info}."
    response = llm.invoke(prompt)

    return {"messages": [response.content],
            "missing_fields": []}
  
def router(state:SupervisorState)->SupervisorState:
    
    complaint_data=state.get("complaint_data",[])
    required_fields=["product", "issue_type", "purchase_date"]
    missing = [field for field in required_fields if not complaint_data.get(field)]

    if missing:
            return Command(
                goto="ask_missing_node", 
                update={
                    "missing_info": missing,
                    "complaint_data":complaint_data
                    } 
                )
    return Command(goto="create_ticket_node")
    
def build_complaint_graph():
    
    complaint_graph = StateGraph(SupervisorState)
    #Add Nodes
    complaint_graph.add_node('extract_info_node', extract_info_node)
    complaint_graph.add_node("ask_missing_node", ask_missing_node)
    complaint_graph.add_node("create_ticket_node",create_ticket_node)
    complaint_graph.add_node("router", router)

    #Add Edges
    complaint_graph.add_edge(START,'extract_info_node')
    complaint_graph.add_edge("extract_info_node","router")
    complaint_graph.add_edge("ask_missing_node",END)
    complaint_graph.add_edge("create_ticket_node",END)
    
    return complaint_graph.compile()

complaint_graph = build_complaint_graph()

def complaint_flow(state:SupervisorState)->SupervisorState:
    
    return complaint_graph.invoke(state)