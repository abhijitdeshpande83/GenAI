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
        outputs = model.generate(**inputs, max_length=64, early_stopping=True)
        predicted_ids = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

        return predicted_ids

def output_fn(predictions, accept):
    
    if accept=="application/json":
        output = {"generated_text": predictions}
        
        return json.dumps(output), accept
    
    elif accept=="application/jsonlines":
        lines = []
        if isinstance(predictions, list):
            for prediction in predictions:
                lines.append(json.dumps({"generated_text": prediction}))
        else:
            lines.append(json.dumps({"generated_text": predictions}))
        
        return "\n".join(lines), accept
    
    else:
        raise ValueError(f"Unsupported Accept header: {accept}")