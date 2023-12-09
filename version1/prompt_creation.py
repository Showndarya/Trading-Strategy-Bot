import json
import pandas as pd

def generate_jsonl_entry(prompt, answer):
    """
    Generate a JSONL entry for fine-tuning.
    """
    return {
        "messages": [
            {"role": "system", "content": "Marv is a factual chatbot that is also an expert in trading, stocks and investments."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": answer}
        ]
    }

def main():
    df = pd.read_csv('data/gpt_training_data.csv')

    df['prompt'] = df['prompt'].astype(str).fillna('')
    df['answer'] = df['answer'].astype(str).fillna('')

    with open('data/training_data.jsonl', 'w') as jsonl_file:
        for index, row in df.iterrows():
            jsonl_entry = generate_jsonl_entry(row['prompt'], row['answer'])
            jsonl_file.write(json.dumps(jsonl_entry) + '\n')

if __name__ == "__main__":
    main()


