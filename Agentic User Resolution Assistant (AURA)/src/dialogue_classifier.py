import torch
from transformers import pipeline

dialogue_classifier = pipeline(
    "zero-shot-classification",
    model="cross-encoder/nli-deberta-v3-small"  
)

# DIALOGUE_LABELS = [
#     "customer reporting something is broken, not working, or malfunctioning",
#     "customer asking a question to get information or learn how to do something",
#     "customer expressing unhappiness or requesting action like return or replacement",
#     "social message like a greeting, goodbye, or unrelated conversation",
#     "customer describing a situation without saying what they want done" 
# ]

DIALOGUE_LABELS = {
    "customer reporting something is broken, not working, or malfunctioning": "complaint_flow",
    "customer asking a question to get information or learn how to do something": "inquiry_node",
    "customer expressing unhappiness or requesting action like return or replacement": "retention_flow",
    "social message like a greeting, goodbye, or unrelated conversation": "greeting_flow",
    "customer describing a situation without saying what they want done": "clarification_flow" 
}

def classify_dialogue_act(message:str)->dict:
    result = dialogue_classifier(
        message,
        candidate_labels=list(DIALOGUE_LABELS.keys()),
        multi_label=False
        )
    label = DIALOGUE_LABELS.get(result['labels'][0],"unknown")
    top_score = result['scores'][0]
    sec_score = result['scores'][1]
    margin = top_score-sec_score

    return label, margin
