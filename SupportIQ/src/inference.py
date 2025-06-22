from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel, PeftConfig
import torch
import glob, os

def get_latest_model(model_dir):
    #get latest model
    checkpoint_path = glob.glob(os.path.join(model_dir, "checkpoint*"))
    
    return sorted(checkpoint_path, key=lambda x: int(x.split('-')[-1]))[-1]
    

def model_fn(model_dir):

    #load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    #load base model & wrap with peft
    # peft_config = PeftConfig.from_pretrained(checkpoint_path)
    # base_model = AutoModelForSeq2SeqLM.from_pretrained(peft_config.base_model_name_or_path)
    # model = PeftModel.from_pretrained(base_model, checkpoint_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model.eval()

    return {'model': model,'tokenizer': tokenizer}

def predict_fn(data, model_obj):
    input_text = data['input']
    tokenizer = model_obj['tokenizer']
    model = model_obj['model']

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # input_text = [item['input'] for item in data]

    inputs = tokenizer(input_text, return_tensors='pt',padding=True, truncation=True).to(device)
    with torch.no_grad():
        outputs =model.generate(**inputs, max_new_tokens=20)
    
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # decoded = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return {'generated_text': decoded}