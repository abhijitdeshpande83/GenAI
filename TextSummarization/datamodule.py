import pytorch_lightning as pl
from torch.utils.data import DataLoader
import pandas as pd
from dataset import SummarizationDataset


class SummarizationDataModule(pl.LightningDataModule):
    def __init__(self,train_path, val_path, tokenizer, batch_size=32,max_length=1024, summary_length=256):
        super().__init__()
        self.train_path = train_path
        self.val_path = val_path
        self.tokenizer = tokenizer
        self.batch_size = batch_size
        self.max_length = max_length
        self.summary_length= summary_length
    
    def setup(self, stage=None):
        train_df = pd.read_csv(self.train_path)
        val_df = pd.read_csv(self.val_path)

        self.train_dataset = SummarizationDataset(train_df, self.tokenizer,
                                                  self.max_length,self.summary_length)
        self.val_dataset = SummarizationDataset(val_df, self.tokenizer,
                                                  self.max_length,self.summary_length)
        
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)
    
    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size, shuffle=False)


