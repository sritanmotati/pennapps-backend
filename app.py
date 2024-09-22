from flask import Flask
from transformers import pipeline
import os
import requests
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def hello_world():
    return 'Hey from Flask!'

@app.route('/sentiment/text=<text>')
def sentiment_analysis(text):
    return sentiment_pipeline(text)

@app.route('/topic/prompt=<prompt>')
def topic_classifier(prompt):
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "sk-tune-LWw4p6Gu8psAwdpVfL4eLkwLtNctxp416KL",
        "Content-Type": "application/json",
    }
    data = {
    "temperature": 0.9,
        "messages":  [
        {
            "role": "system",
            "content": "You will be given text from reviews on a restaurant. Classify the main focus of the review as either food, service, or environment. Only provide the one word answer."
        },
        {
            "role": "user",
            "content": prompt,
        }
        ],
        "model": "meta/llama-3.1-8b-instruct",
        "stream": False,
        # "frequency_penalty":  0.2,
        "max_tokens": 4
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

@app.route('/cerebras/prompt=<prompt>')
def cerebras(prompt):
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "sk-tune-LWw4p6Gu8psAwdpVfL4eLkwLtNctxp416KL",
        "Content-Type": "application/json",
    }
    data = {
    "temperature": 0.9,
        "messages":  [
        {
            "role": "system",
            "content": "You are an expert on maximizing small businesses. You will be given metrics and reviews and such data. Sometimes you will be asked to give recommendations for the business to improve, other times you will simply summarize what you're given."
        },
        {
            "role": "user",
            "content": prompt,
        }
        ],
        "model": "meta/llama-3.1-8b-instruct",
        "stream": False,
        # "frequency_penalty":  0.2,
        # "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)