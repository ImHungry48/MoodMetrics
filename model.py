from transformers import pipeline

model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis', model=model_id)

def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text)
        return result
    except Exception as e:
        # Log the exception for debugging
        print(f"Model Error: {e}")
        return {'error': 'An error occurred during sentiment analysis'}
