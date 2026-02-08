from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json

def model_fn(model_uri):
    
    tokenizer = AutoTokenizer.from_pretrained(model_uri)                          #load tokenizer
    
    model = AutoModelForSequenceClassification.from_pretrained(model_uri)         #load model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return {'model': model,'tokenizer': tokenizer, 'device':device}

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        data = json.loads(request_body)
        return data["input"]
    elif request_content_type == "application/jsonlines":
        return [json.loads(line)["input"] for line in request_body.strip().split("\n")]
    else:
        return ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_text, model_obj):

    if input_text is None:
        raise ValueError("Inpute text is required under key 'input'")
    
    tokenizer = model_obj['tokenizer']
    model = model_obj['model']
    device = model_obj['device']

    if isinstance(input_text,list):
        inputs = tokenizer(input_text, return_tensors='pt',padding=True, truncation=True).to(device)
    else:
        inputs = tokenizer([input_text], return_tensors='pt',padding=True, truncation=True).to(device)

    with torch.no_grad():
        logits = model(**inputs).logits
        predicted_ids = logits.argmax(dim=-1)
        probs = torch.nn.functional.softmax(logits, dim=-1)
    
    results = []
    for i, pred in enumerate(predicted_ids):
        class_label = model.config.id2label[pred.item()]
        score = probs[i, pred].item()
        results.append({"label": class_label, "score": score})

    return results if isinstance(input_text,list) else results[0]
