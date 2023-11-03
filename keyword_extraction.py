import pandas as pd
import yake
import csv

df = pd.read_csv('reddit_data.csv')
keywords = set()
text = ""
kw_extractor = yake.KeywordExtractor()

print('Generating keywords...')

for i in range(len(df)):
    post = df.iloc[i]
    title_content = str(post[2]) + " " + str(post[3]) # title concatenated with content
    title_content = title_content.replace("’", "'")
    text += title_content.lower() + " "

extracted_keywords = kw_extractor.extract_keywords(text)
for extracted_keyword in extracted_keywords:
    keywords.add(extracted_keyword[0])

print('Keywords generated!')

with open('keywords.csv', 'w') as keyword_file:
    writer = csv.writer(keyword_file)
    for keyword in keywords:
        writer.writerow([keyword])