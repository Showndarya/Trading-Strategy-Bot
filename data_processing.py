import pandas as pd
import re
import nltk
import json
nltk.download('punkt')
from acronyms import acronyms
from sentiment_analysis import SentimentAnalyzer
from post_comment_keyword_extraction import KeywordExtraction
from stock_market_acronyms import stock_market_acronyms

with open('stocks_data.json', 'r') as jsonfile:
    stock_acronyms = json.load(jsonfile)

def clean_text(text):
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower().strip()
    return text

def expand_acronyms(text):
    for acronym, expansion in acronyms.items():
        text = re.sub(r'\b' + acronym + r'\b', expansion, text)

    for stock_market_acronym, stock_market_expansion in stock_market_acronyms.items():
        text = re.sub(r'\b' + stock_market_acronym + r'\b', stock_market_expansion, text)
    
    for stock_market_acronym, stock_market_expansion in stock_market_acronyms.items():
        text = re.sub(r'\b' + stock_market_acronym + r'\b', stock_market_expansion, text)

    for stock_acronym, stock_expansion in stock_acronyms.items():
        text = re.sub(r'\b' + stock_acronym + r'\b', stock_expansion, text)

    return text

df = pd.read_csv('data/reddit_data.csv')

columns_to_process = ['content', 'top_comment_1', 'top_comment_2', 'top_comment_3']
for column in columns_to_process:
    df[column] = df[column].apply(lambda x: clean_text(str(x)))
    df[column] = df[column].apply(expand_acronyms)

sentiment_analyzer = SentimentAnalyzer()
keyword_extractor = KeywordExtraction()

for column in columns_to_process:
    df[column + '_sentiment'] = df[column].apply(lambda x: sentiment_analyzer.extract_sentiment_score([x])[0])
    df[column + '_keywords'] = df[column].apply(lambda x: keyword_extractor.extract_keywords([x])[0])  # Extracting keywords

gpt_dataset = pd.DataFrame()
for index, row in df.iterrows():
    prompt = row['content']
    for i in range(1, 4):
        answer = row[f'top_comment_{i}']
        sentiment_score = row[f'top_comment_{i}_sentiment']
        keywords = row[f'top_comment_{i}_keywords']
        gpt_dataset = gpt_dataset.append({
            'prompt': prompt,
            'answer': answer,
            'sentiment_score': sentiment_score,
            'keywords': keywords
        }, ignore_index=True)

gpt_dataset.to_csv('data/gpt_training_data.csv', index=False)

# tfidf
# df['tokens'] = df['content'].apply(word_tokenize)
# df['text'] = df['tokens'].apply(lambda tokens: ' '.join(tokens))
# vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
# tfidf_matrix = vectorizer.fit_transform(df['text'])
# feature_names = vectorizer.get_feature_names_out()
# tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
# tfidf_df['title'] = df['title']
# print(tfidf_df.head())
# tfidf_df.to_csv('tfidf_results.csv', index=False)