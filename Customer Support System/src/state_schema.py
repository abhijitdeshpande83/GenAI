<<<<<<< HEAD
<<<<<<< HEAD
from typing import Annotated, Dict, Optional
=======
from typing import Annotated, Dict
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)
=======
from typing import Annotated, Dict, Optional
>>>>>>> ff55703 (feat: implement active_flow flag for state-aware subgraph persistence)
from operator import add
from langgraph.graph import MessagesState

def merge_dicts(left:dict, right:dict)->dict:

<<<<<<< HEAD
    if right=={}:
        return {}
=======
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)
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
<<<<<<< HEAD
<<<<<<< HEAD
    active_flow: Optional[str]=None
    customer_profile: Dict
=======
    next: str
    customer_profile: Dict
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)
=======
    active_flow: Optional[str]=None
    customer_profile: Dict
>>>>>>> ff55703 (feat: implement active_flow flag for state-aware subgraph persistence)
