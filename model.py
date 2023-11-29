import pandas as pd
import json
import openai
openai.api_key = ''

df = pd.read_csv('data/gpt_training_data.csv')

df['prompt'] = df['prompt'].astype(str).fillna('')

with open('data/fine_tune_data.jsonl', 'w') as jsonl_file:
    for index, row in df.iterrows():
        if isinstance(row['keywords'], list):
            keywords = ', '.join(row['keywords'])
        else:
            keywords = row['keywords']
        
        data = {
            "prompt": row['prompt'],
            "completion": f"{row['answer']} [Sentiment: {row['sentiment_score']}] [Keywords: {keywords}]"
        }
        jsonl_file.write(json.dumps(data) + '\n')



result = openai.FineTune.create(
    training_file='',   
    model='gpt-3.5-turbo',            
    n_epochs=3,                       
    learning_rate_multiplier=0.1,     
    batch_size=4,                     
    prompt_loss_weight=0.1,           
    compute_classification_metrics=False,  
    # classification_n_classes=None,    
    # classification_positive_class=None,  
    classification_betas=(0.5, 0.5),  
    # p=0.1,                            
    # max_tokens=100,                   
    use_packing=True,                 
    # validation_file=None             
)

print(result)