from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from src.state_schema import SupervisorState
from src.supervisor_graph import supervisor_node
from src.complaint_graph import complaint_flow
from src.inquiry_graph import inquiry_flow
from src.retention_graph import retention_flow
from src.conversation_graph import greeting_flow, clarification_flow

def build_graph():

    graph = StateGraph(SupervisorState)

    graph.add_node("supervisor",supervisor_node)
    graph.add_node("greeting_flow",greeting_flow)
    graph.add_node("clarification_flow", clarification_flow)
    graph.add_node("complaint_flow", complaint_flow)
    graph.add_node("retention_flow", retention_flow)
    graph.add_node("inquiry_flow", inquiry_flow)

    graph.add_edge(START, "supervisor")
    graph.add_edge("greeting_flow", END)
    graph.add_edge("clarification_flow", END)

    memory = MemorySaver()
    return graph.compile(checkpointer=memory)

workflow = build_graph()

def agent(user_input: str, thread_id:str)->SupervisorState:
    config = {"configurable": {"thread_id": thread_id}}
    return workflow.invoke(
        {"user_input":user_input},
        config
        )
