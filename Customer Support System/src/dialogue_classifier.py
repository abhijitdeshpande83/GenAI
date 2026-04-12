import torch
from transformers import pipeline
dialogue_classifier = pipeline(
    "zero-shot-classification",
    model="cross-encoder/nli-deberta-v3-small"  
)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ff55703 (feat: implement active_flow flag for state-aware subgraph persistence)
# DIALOGUE_LABELS = [
#     "customer reporting something is broken, not working, or malfunctioning",
#     "customer asking a question to get information or learn how to do something",
#     "customer expressing unhappiness or requesting action like return or replacement",
#     "social message like a greeting, goodbye, or unrelated conversation",
#     "customer describing a situation without saying what they want done" 
# ]
<<<<<<< HEAD

DIALOGUE_LABELS = {
=======
DIALOGUE_LABELS = [
    "customer reporting something is broken, not working, or malfunctioning",
    "customer asking a question to get information or learn how to do something",
    "customer expressing unhappiness or requesting action like return or replacement",
    "social message like a greeting, goodbye, or unrelated conversation",
    "customer describing a situation without saying what they want done" 
]

mapper = {
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)
=======

DIALOGUE_LABELS = {
>>>>>>> ff55703 (feat: implement active_flow flag for state-aware subgraph persistence)
    "customer reporting something is broken, not working, or malfunctioning": "complaint_flow",
    "customer asking a question to get information or learn how to do something": "inquiry_node",
    "customer expressing unhappiness or requesting action like return or replacement": "retention_flow",
    "social message like a greeting, goodbye, or unrelated conversation": "greeting_flow",
    "customer describing a situation without saying what they want done": "clarification_flow" 
}

def classify_dialogue_act(message:str)->dict:
    result = dialogue_classifier(
        message,
<<<<<<< HEAD
<<<<<<< HEAD
        candidate_labels=list(DIALOGUE_LABELS.keys()),
        multi_label=False
        )
    label = DIALOGUE_LABELS.get(result['labels'][0],"unknown")
    top_score = result['scores'][0]
    sec_score = result['scores'][1]
    margin = top_score-sec_score

    return label, margin
=======
        candidate_labels=DIALOGUE_LABELS,
=======
        candidate_labels=list(DIALOGUE_LABELS.keys()),
>>>>>>> ff55703 (feat: implement active_flow flag for state-aware subgraph persistence)
        multi_label=False
        )
    label = DIALOGUE_LABELS.get(result['labels'][0],"unknown")
    top_score = result['scores'][0]
    sec_score = result['scores'][1]
    margin = top_score-sec_score

<<<<<<< HEAD
    return label, score
>>>>>>> a3ec9ed (feat: modularize agent logic into domain-specific subgraphs)
=======
    return label, margin
>>>>>>> ff55703 (feat: implement active_flow flag for state-aware subgraph persistence)

