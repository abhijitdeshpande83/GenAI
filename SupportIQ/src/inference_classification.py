from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
import boto3

def model_fn():

    local_dir = "/app/model/"

    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    
    # s3 = boto3.client('s3')
    # objects = s3.list_objects_v2(Bucket=s3_bucket, Prefix=s3_prefix)
    
    # for obj in objects.get("Contents", []):
    #     key = obj['Key']
    #     if key.endswith("/"):
    #         continue
    #     file_name = os.path.basename(key)
    #     local_path = os.path.join(local_dir, file_name)
    #     s3.download_file(s3_bucket, key, local_path)

    tokenizer = AutoTokenizer.from_pretrained(local_dir)                          #load tokenizer
    
    model = AutoModelForSequenceClassification.from_pretrained(local_dir)         #load model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return {'model': model,'tokenizer': tokenizer, 'device':device}


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

def predict(input_text):
    model_obj = model_fn()
    return predict_fn(input_text, model_obj)



