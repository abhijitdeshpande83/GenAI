from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments)
from peft import LoraConfig, get_peft_model, TaskType
import torch
import argparse 
import os
from utils.loader import tokenize_data

def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_path', type=str, default=os.path.join(os.environ.get("SM_CHANNEL_TRAINING"),'data_full.json'))
    parser.add_argument('--model_id', type=str, default='google/flan-t5-base')
    parser.add_argument('--rank', type=int, default=8)
    parser.add_argument('--alpha', type=int, default=16)
    parser.add_argument('--dropout', type=float, default=0.05)
    parser.add_argument('--bias', type=str, default='none')
    parser.add_argument('--output_dir', type=str, default=os.environ.get("SM_MODEL_DIR", "./output"))
    parser.add_argument('--lr', type=float, default=1e-5)
    parser.add_argument('--epochs', type=int, default=1)
    parser.add_argument('--wd', type=float, default=0.01)
    parser.add_argument('--logging_steps', type=int, default=1)
    parser.add_argument('--batch_size', type=int, default=32)

    arg = parser.parse_args()
    
    #load model & tokeninzer
    model_id = arg.model_id
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

    #load tokinzed data
    train_data, val_data, test_data = tokenize_data(arg.data_path, tokenizer)

    #setup training args
    lora_config = LoraConfig(
                    r=arg.rank,
                    lora_alpha=arg.alpha,
                    target_modules=["q", "v"],  # for flan-t5
                    lora_dropout=arg.dropout,
                    bias=arg.bias,
                    task_type=TaskType.SEQ_2_SEQ_LM,
                )
    
    #wrapping LoRA-config model
    peft_model = get_peft_model(model,lora_config) 
    
    
    training_args = TrainingArguments(
                output_dir=arg.output_dir,
                learning_rate=arg.lr,
                num_train_epochs=arg.epochs,
                weight_decay=arg.wd,
                logging_steps=arg.logging_steps,
                label_names=["labels"],
                )
    
    #define trainer
    trainer = Trainer(
            model=peft_model,
            args=training_args,
            train_dataset=train_data,
            eval_dataset=val_data,
            tokenizer=tokenizer,
            )

    trainer.train()

if __name__=='__main__':
    main()