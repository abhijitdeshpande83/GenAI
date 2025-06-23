import json
from datasets import Dataset

def format_data(data):
    return {
        "input": f"Classify the intent: {data[0]}",
        "output": data[1]
    }

def load_data(path='data/data_full.json'):
    with open(path) as f:
        data = json.load(f)

    data['train'].extend(data['oos_train'])
    data['val'].extend(data['oos_val'])
    # data['test'].extend(data['oos_test'])     #exluding test data

    train_data = Dataset.from_list([format_data(x) for x in data['train']])
    val_data = Dataset.from_list([format_data(x) for x in data['val']])
    # test_data = Dataset.from_list([format_data(x) for x in data['test']])

    return train_data, val_data


def tokenize_data(path,tokenizer):
    train_data, val_data = load_data(path)

    def tokenize(data):
        return tokenizer(
            data['input'],
            text_target=data['output'],
            padding='max_length',
            truncation=True,
            max_length=32
        )
    
    return train_data.map(tokenize), val_data.map(tokenize)
