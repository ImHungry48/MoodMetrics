import logging
from transformers import pipeline

model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis', model=model_id)

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text)
        return result
    except Exception as e:
        # Log the exception for debugging
        logging.error(f"Model Error: {e}")
        return {'error': 'An error occurred during sentiment analysis'}
