
import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer


class SummarizationDataset(Dataset):
    """
    Handles tokenization and dataset creation.
    """
    def __init__(self, data, tokenizer, max_length=1024, summary_length=256):
        self.data = data
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.max_length = max_length
        self.summary_length= summary_length

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        input_text = self.data.iloc[index]['document']
        summary_text = self.data.iloc[index]['summary']

        tokenized_inputs = self.tokenizer(
            input_text, max_length=self.max_length,padding='max_length', truncation=True, return_tensors='pt'
        )

        tokenized_labels =  self.tokenizer(
            summary_text, max_length=self.summary_length,padding='max_length', truncation=True, return_tensors='pt'
        )

        return {
            "input_ids": tokenized_inputs["input_ids"].squeeze(0),
            "attention_mask":tokenized_inputs["attention_mask"].squeeze(0),
            "labels": tokenized_labels["input_ids"].squeeze(0)
        }
