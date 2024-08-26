# MoodMetrics
## Overview

This project is a simple Flask web application that performs sentiment analysis on text inputs using a pre-trained sentiment analysis model from the `transformers` library. The application exposes two endpoints:
- `\` - A welcome message
- `/analyze` - An endpoint to analyze the sentiment of the provided text/

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- `pip` (Python package installer)

## Usage
Welcome Endpoint
- URL: /
- Method: GET
- Response: A simple welcome message.
```
curl http://127.0.0.1:5000/
```
- Response:
```
Welcome to the Sentiment Analysis Dashboard!
```
Analyze Endpoint
- URL: /analyze
- Method: POST
- Content-Type: application/json
- Request Body: JSON object containing the text to analyze.
Example request:
```
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "I love you."}'
```
Response:
```
[
  {
    "label": "POSITIVE",
    "score": 0.9998
  }
]
```
The response will be a JSON object with a sentiment label and score.

## Error Handling
- 404 Bad Request: Returned if no text is provided in the request.
- 500 Internal Server Error: Returned if an unexpected error occurs during sentiment analysis.

## Troubleshooting
- Ensure Dependencies: Make sure all required Python packages are installed correctly.
- Check Logs: Review the terminal logs for error messages if the application isn't behaving as expected.
- Verify JSON Payload: Ensure the JSON payload is correctly formatted when making POST requests.