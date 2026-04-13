from langgraph.types import Command
from src.state_schema import SupervisorState
from src.dialogue_classifier import classify_dialogue_act

# Supervisor Node
def supervisor_node(state:SupervisorState)->SupervisorState:

    history = state.get("observations", [])
    user_input = state.get("user_input")
    current_intent = state.get("user_intent", "unknown")
    active_flow = state.get("active_flow", [])
    print("active_flow -->", active_flow)
    if active_flow:
        return Command(goto=active_flow)

    label, margin = classify_dialogue_act(user_input)

    f"active_flow: {active_flow}, margin: {margin}, label: {label}"
    if margin>=0.12:
        return Command(goto=label, 
                       update={"active_flow":label}
                       )
    else:
        return Command(goto="clarification_flow")
    
    
