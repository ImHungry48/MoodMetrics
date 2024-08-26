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
