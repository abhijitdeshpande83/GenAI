from langgraph.types import Command
from src.state_schema import SupervisorState
from src.dialogue_classifier import classify_dialogue_act

# Supervisor Node
def supervisor_node(state:SupervisorState)->SupervisorState:

    history = state.get("observations", [])
    user_input = state.get("user_input")
    current_intent = state.get("user_intent", "unknown")

    label, score = classify_dialogue_act(user_input)

    print(score)
    if score>=0.4:
        return Command(goto=label)
    else:
        return Command(goto="clarification_flow")
    
    
