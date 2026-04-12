from typing import Annotated, Dict, Optional
from operator import add
from langgraph.graph import MessagesState

def merge_dicts(left:dict, right:dict)->dict:

    if not right: return left
    if not left: return right

    def is_empty(v):
        return v is None or str(v).strip().lower() in ("none","null","")

    return {**left, **{k:v for k,v in right.items() if not is_empty(v)}}

class SupervisorState(MessagesState):
    """
        State for multi-agent system
    """   
    user_input: str
    user_intent: str

    actions_taken: str
    observations: Annotated[list, add]
    response: Annotated[list, add]
    
    complaint_data: Annotated[dict, merge_dicts]
    missing_info: list
    active_flow: Optional[str]=None
    customer_profile: Dict
