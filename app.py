
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from transformers import pipeline
import os
from cerebras.cloud.sdk import Cerebras

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")
client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/sentiment/text=<text>')
def sentiment_analysis(text):
    return sentiment_pipeline(text)

@app.route('/cerebras/prompt=<prompt>')
def cerebras(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3.1-8b",
    )
    return chat_completion

if __name__ == '__main__':
    app.run()