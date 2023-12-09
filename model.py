import pandas as pd
import json
import openai
import config

openai.api_key = ''

result = openai.fine_tuning.jobs.create(
    training_file='file-fZlAEImaowVhBGgq4JiOxy4c',   
    model='gpt-3.5-turbo',            
    hyperparameters= {
      "n_epochs": 2,
    },                            
    # batch_size=4,                     
    # prompt_loss_weight=0.1,           
    # compute_classification_metrics=False,  
    # classification_n_classes=None,    
    # classification_positive_class=None,  
    # classification_betas=(0.5, 0.5),  
    # p=0.1,                            
    # max_tokens=100,                   
    # use_packing=True,                 
    # validation_file=None             
)

print(result)