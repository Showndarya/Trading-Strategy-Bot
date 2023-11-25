import pandas as pd
import yake

class KeywordExtraction():
    def __init__(self):
        super(KeywordExtraction, self).__init__()
        self.kw_extractor = yake.KeywordExtractor(top=5) # top 5 keywords

    # text is an array of 4 arrays (post text, top 3 comments)
    def extract_keywords(self, texts):
        keywords = []
        for text in texts:
            text = text.lower()
            extracted_keywords = self.kw_extractor.extract_keywords(text)
            keywords_text = [extracted_keyword[0] for extracted_keyword in extracted_keywords]
            keywords.append(keywords_text)

        return keywords

