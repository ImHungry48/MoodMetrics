from flask import Flask, request, jsonify
from model import analyze_sentiment  # Import the function from your model script

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis Dashboard!"

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the text data from the POST request
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Perform sentiment analysis
    result = analyze_sentiment(text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
