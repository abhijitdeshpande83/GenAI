import pytorch_lightning as pl
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, AdamW

class SummarizationModel(pl.LightningModule):
    def __init__(self, model_name, lr=1e-5):
        super().__init__()
        self.save_hyperparameters()
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.lr = lr
        for param in self.model.parameters():
            param.requires_grad = True 

    def forward(self, input_ids, attention_mask, labels=None):
        return self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
    
    def training_step(self, batch, batch_idx):
        outputs = self(
                    input_ids=batch["input_ids"], 
                    attention_mask=batch["attention_mask"], 
                    labels=batch["labels"])       
        loss = outputs.loss
        self.log("train_loss", loss, prog_bar=True)
        return loss
    
    def validation_step(self, batch, batch_idx):
        outputs = self(
                    input_ids=batch["input_ids"], 
                    attention_mask=batch["attention_mask"], 
                    labels=batch["labels"])         
        val_loss = outputs.loss
        self.log("val_loss", val_loss, prog_bar=True)
        return val_loss
    
    def configure_optimizers(self):
        return AdamW(self.parameters(), lr=self.lr)


