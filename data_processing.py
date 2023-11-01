from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower().strip() 
    return text

df = pd.read_csv('reddit_data.csv')
df['content'] = df['content'].apply(lambda x: clean_text(str(x)))
df['tokens'] = df['content'].apply(word_tokenize)


df['text'] = df['tokens'].apply(lambda tokens: ' '.join(tokens))
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['text'])
feature_names = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
tfidf_df['title'] = df['title']
print(tfidf_df.head())
tfidf_df.to_csv('tfidf_results.csv', index=False)
