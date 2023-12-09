from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer():
    def __init__(self):
        super(SentimentAnalyzer, self).__init__()
        self.sia = SentimentIntensityAnalyzer()

    def extract_sentiment_score(self, texts):
        sentiment_scores = []
        for text in texts:
            sentiment_score = self.sia.polarity_scores(text)
            sentiment_scores.append(sentiment_score)
        
        return sentiment_scores