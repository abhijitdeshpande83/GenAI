from transformers import T5Tokenizer, T5ForConditionalGeneration
from peft import PeftModel, PeftConfig
import torch
import glob, os
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

    tokenizer = T5Tokenizer.from_pretrained(local_dir)                           #load tokenizer
    model = T5ForConditionalGeneration.from_pretrained(local_dir)                #load model
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

    inputs = tokenizer(input_text, return_tensors='pt',padding=True, truncation=True).to(device)
    with torch.no_grad():
        outputs =model.generate(**inputs, max_new_tokens=20)
    
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return {'generated_text': decoded}

def predict(input_text):
    model_obj = model_fn()
    return predict_fn(input_text, model_obj)