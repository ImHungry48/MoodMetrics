from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result
