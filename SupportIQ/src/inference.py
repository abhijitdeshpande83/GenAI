from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel, PeftConfig
import torch

def model_fn(model_dir):

    #load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    #load base model & wrap with peft
    peft_config = PeftConfig.from_pretrained(model_dir)
    base_model = AutoModelForSeq2SeqLM.from_pretrained(peft_config.base_model_name_or_path)
    model = PeftModel.from_pretrained(base_model, model_dir)
    model.eval()

    return {'model': model,'tokenizer': tokenizer}

def predict_fn(data, model_obj):
    input_text = data['inputs']
    tokenizer = model_obj['tokenizer']
    model = model_obj['model']

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    inputs = tokenizer(input_text, return_tensors='pt').to(device)
    with torch.no_grad():
        outputs =model.generate(**inputs, max_new_tokens=50)
    
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {'generated_text': decoded}