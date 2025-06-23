from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments, EarlyStoppingCallback
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
    parser.add_argument('--save_steps', type=int, default=500)
    parser.add_argument('--eval_steps', type=int, default=100)
    parser.add_argument('--early_stopping', type=int, default=3)
    parser.add_argument('--target_module', type=lambda s:s.split(','), default=['q','v'])

    arg = parser.parse_args()
    
    #load model & tokeninzer
    model_id = arg.model_id
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

    #load tokinzed data
    train_data, val_data = tokenize_data(arg.data_path, tokenizer)

    #setup training args
    lora_config = LoraConfig(
                    r=arg.rank,
                    lora_alpha=arg.alpha,
                    target_modules=arg.target_module,  # for flan-t5
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
                evaluation_strategy="steps",
                eval_steps=arg.eval_steps,
                save_strategy="steps",
                save_steps=arg.save_steps,
                per_device_train_batch_size=arg.batch_size,
                per_device_eval_batch_size=arg.batch_size,
                load_best_model_at_end=True,
                metric_for_best_model="eval_loss",
                greater_is_better=False
                )
    
    #define trainer
    trainer = Trainer(
            model=peft_model,
            args=training_args,
            train_dataset=train_data,
            eval_dataset=val_data,
            tokenizer=tokenizer,
            )
    
    #Early stopping
    trainer.add_callback(EarlyStoppingCallback(early_stopping_patience=arg.early_stopping))

    #Train the model
    trainer.train()

    #merge LoRA weights with base model and save
    merged_model = peft_model.merge_and_unload()
    merged_model.save_pretrained(arg.output_dir)
    tokenizer.save_pretrained(arg.output_dir)

if __name__=='__main__':
    main()