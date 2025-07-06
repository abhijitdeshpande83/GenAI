import json
from datasets import Dataset

def format_data(data, task_type='classification'):
    if task_type=='classification':
        return {
            "input": data[0],
            "label": data[1]
            }
    elif task_type=='seq2seq':
        return {
            "input": f"Classify the intent: {data[0]}",
            "output": data[1]
            }
    else:
        raise ValueError("task_type must be either classification or seq2seq")

def load_data(path='data/data_full.json', task_type='classification'):
    with open(path) as f:
        data = json.load(f)

    data['train'].extend(data['oos_train'])
    data['val'].extend(data['oos_val'])

    train_data = Dataset.from_list([format_data(x,task_type) for x in data['train']])
    val_data = Dataset.from_list([format_data(x,task_type) for x in data['val']])

    return train_data, val_data

def tokenize_data(path,tokenizer,task_type,max_length):
    train_data, val_data = load_data(path,task_type)
    if task_type=='classification':
        labels = sorted(set(train_data['label']))
        label2id = {label:i for i,label in enumerate(labels)}
        id2label = {i:label for i,label in enumerate(labels)}
  

    def tokenize_for_seq2seq(data):
        return tokenizer(
            data['input'],
            text_target=data['output'],
            padding='max_length',
            truncation=True,
            max_length=max_length
        )
    
    def tokenize_for_classification(data):
        model_inputs = tokenizer(
            data['input'],
            padding='max_length',
            truncation=True,
            max_length=max_length,
            )
        
        model_inputs['labels'] = label2id[data['label']]
        return model_inputs
    
    if task_type=='classification':
        tokenized_train_data = train_data.map(tokenize_for_classification) 
        tokenized_val_data = val_data.map(tokenize_for_classification) 
        tokenized_train_data.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
        tokenized_val_data.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
        return tokenized_train_data, tokenized_val_data, label2id, id2label
    
    elif task_type=='seq2seq':
        tokenized_train_data = train_data.map(tokenize_for_seq2seq)
        tokenized_val_data = val_data.map(tokenize_for_seq2seq)
        tokenized_train_data.set_format(type="torch")
        tokenized_val_data.set_format(type="torch")
        return tokenized_train_data, tokenized_val_data, None, None
    
    else:
        raise ValueError("task_type must be either classification or seq2seq")
