import pandas as pd

reddit_data = pd.read_csv('reddit_data.csv')

messages = reddit_data['title'].tolist()
responses = reddit_data['content'].tolist()

# pip install transformers

# can use this to fine tune gpt 3 https://github.com/norahsakal/fine-tune-gpt3-model/blob/main/fine_tune_step_by_step.ipynb