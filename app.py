from flask import Flask
from transformers import pipeline
import os
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")

client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)

@app.route('/')
def hello_world():
    return 'Hey from Flask!'

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
    return chat_completion.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True, port=3000)