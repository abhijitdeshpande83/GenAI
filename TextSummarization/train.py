import pytorch_lightning as pl
import os
import argparse
from transformer_model import SummarizationModel
from datamodule import SummarizationDataModule

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--train_data_path', type=str, default=os.path.join(os.environ.get('SM_CHANNEL_TRAINING'), 'train_10k.csv'))
    parser.add_argument('--val_data_path', type=str, default=os.path.join(os.environ.get('SM_CHANNEL_VALIDATION'), 'val.csv'))
    parser.add_argument('--model_name', type=str, default='facebook/bart-base')
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--max_length', type=int, default=1024)
    parser.add_argument('--summary_length', type=int, default=128)
    parser.add_argument('--lr', type=float, default=2e-5)
    parser.add_argument('--epochs', type=int, default=1)

    arg = parser.parse_args()

    data_module = SummarizationDataModule(
        train_path=arg.train_data_path,
        val_path=arg.val_data_path,
        tokenizer=arg.model_name,
        batch_size=arg.batch_size,
        max_length=arg.max_length,
        summary_length=arg.summary_length 
        )

    model = SummarizationModel(arg.model_name, lr=arg.lr)

    trainer = pl.Trainer(
        max_epochs=arg.epochs,
        accelerator="auto",  # Set to "cpu" if no GPU available
        devices=1,
        precision=16,  # Mixed precision training
        callbacks=[pl.callbacks.ModelCheckpoint(dirpath=os.environ.get('SM_MODEL_DIR'))],
        logger=pl.loggers.TensorBoardLogger(save_dir=os.environ.get('SM_OUTPUT_DIR'))
        )

    trainer.fit(model, datamodule=data_module)

if __name__ == '__main__':
    main()