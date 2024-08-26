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

sentiment_analyzer = pipeline('sentiment-analysis', model=model_id)

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text)
        return result
    except Exception as e:
        logging.error(f"Model Error: {e}")
        return {'error': 'An error occurred during sentiment analysis'}
```

### `app.py`

This script sets up the Flask web server and defines routes for the web application.

```python
from flask import Flask, request, render_template, jsonify
from model import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text')
    
    if not text:
        return render_template('index.html', error='No text provided')

    result = analyze_sentiment(text)
    
    return render_template('index.html', result=result)

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
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        textarea {
            width: 100%;
            max-width: 600px;
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        pre {
            background: #fff;
            border: 1px solid #ddd;
            padding: 10px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Sentiment Analysis Dashboard</h1>
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
</body>
</html>
```