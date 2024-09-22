from flask import Flask
from transformers import pipeline
import os
import requests
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebaseServiceKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# from dotenv import load_dotenv

# load_dotenv()

from async_scraper import async_scrape

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def hello_world():
    return 'Welcome to mtrx!'

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

@app.route('/suggestions/prompt=<prompt>')
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

@app.route('/db/competitors/business_id=<business_id>')
def get_competitors(business_id):
    doc_ref = db.collection("businesses").document(business_id)
    doc = doc_ref.get().to_dict()
    tags = doc["business_tags"]
    
    # find businesses with shared tags
    competitors = {}
    for tag in tags:
        for doc in db.collection("businesses").where("business_tags", "array_contains", tag).stream():
            if doc.id in competitors:
                competitors[doc.id] += 1
            else:
                competitors[doc.id] = 1
    # sort by number of shared tags, descending order, give as list
    competitors = [k for k, v in sorted(competitors.items(), key=lambda item: item[1], reverse=True) if k != business_id]
    if len(competitors) > 2:
        return competitors[:2]
    return competitors
    
@app.route('/yelp/url=<url>')
def yelp(url):
    return async_scrape(url.replace('"', ''), 5)

if __name__ == '__main__':
    app.run(debug=True, port=5000)