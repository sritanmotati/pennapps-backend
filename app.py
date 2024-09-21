
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from transformers import pipeline

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/sentiment/text=<text>')
def sentiment_analysis(text):
    return sentiment_pipeline(text)

if __name__ == '__main__':
    app.run()