from flask import Flask, request, render_template
from predict import predict_sentiment
from youtube import get_video_comments
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def get_video(video_id):
    if not video_id:
        return {"error" : "video_id is required"}
    
    comments = get_video_comments(video_id)
    predictions  = predict_sentiment(comments)

    positive = predictions.count("Positive")
    negative = predictions.count("Negative")

    summary = {
        "positive" : positive,
        "negative" : negative,
        "num_comments" : len(comments),
        "rating" : (positive/len(comments))*100
    }

    return {"predictions" : predictions, "comments" : comments, "summary" : summary}


