# MoodMetrics: Real-Time Sentiment Analysis

## Overview

MoodMetrics is a web-based application designed to analyze the sentiment of user inputs in real-time. Users can enter text directly into the application, which will then display sentiment analysis results on a user-friendly dashboard.

## Features

- Real-time sentiment analysis of user input.
- Displays sentiment analysis results on the web dashboard.
- Built with Flask for the web application and Hugging Face's Transformers for sentiment analysis.

## Installation

To set up MoodMetrics on your local machine, follow these steps:

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Dependencies

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/MoodMetrics.git
    cd MoodMetrics
    ```

2. **Install the required packages**

    For PyTorch:

    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```

    For other dependencies:

    ```bash
    pip install numpy<2
    pip install flask transformers
    ```

## Running the Application

1. **Start the Flask server**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to**

    ```
    http://127.0.0.1:5000
    ```

3. **Use the text box on the web page to input text and click "Analyze" to view the sentiment analysis results.**

## API Usage

You can also interact with the sentiment analysis API using `curl` or PowerShell.

### Using `curl`

```bash
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d "{\"text\": \"I love you.\"}"
```

### Using PowerShell

```powershell
$uri = "http://127.0.0.1:5000/analyze"
$body = @{
    text = "I love you."
} | ConvertTo-Json

Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/json"
```

## Project Structure

- **model.py**: Contains the sentiment analysis model and function.
- **app.py**: The main Flask application file.
- **templates/index.html**: The HTML template for the web interface.

### `model.py`

This script initializes a sentiment analysis pipeline using Hugging Face's Transformers library and defines a function to analyze sentiment.

```python
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
```

### `app.py`

This script sets up the Flask web server and defines routes for the web application.

```python
from flask import Flask, request, render_template, jsonify
from model import analyze_sentiment  # Import the function from the model script

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text')  # Get the text from the form submission
    
    if not text:
        return render_template('index.html', error='No text provided')  # Return an error message if no text is provided

    # Perform sentiment analysis
    result = analyze_sentiment(text)
    
    return render_template('index.html', result=result)  # Render the results on the same page

if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html`

This HTML file provides a simple form for text input and displays the sentiment analysis results.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h2>Welcome to Mood Metrics!</h2>
        <p>This tool is designed to help you quickly understand the emotional tone of any text you input.</p>
        <form action="/analyze" method="post">
            <label for="text">Enter text:</label>
            <textarea id="text" name="text" rows="4" cols="50"></textarea>
            <br>
            <button type="submit">Analyze</button>
        </form>

        {% if result %}
            <h2>Analysis Result:</h2>
            <pre>{{ result | tojson(indent=2) }}</pre>
        {% elif error %}
            <h2 class="error">Error:</h2>
            <p>{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
```