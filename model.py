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
        return format_result(result)
    except Exception as e:
        # Log the exception for debugging
        logging.error(f"Model Error: {e}")
        return {'error': 'An error occurred during sentiment analysis'}

def format_result(result):
    try:
        label_result = result[0].get('label')
        formatted_result = ''

        print(label_result)
        if label_result == "positive":
            formatted_result = "Positive"
        elif label_result == "negative":
            formatted_result = "Negative"
        elif label_result == "neutral":
            formatted_result = "Neutral"
        else:
            raise Exception
        return formatted_result
    except Exception as e:
        return {'error': 'An error occurred during result formatting'}