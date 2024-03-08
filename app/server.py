from flask import Flask, request, render_template
from predict import predict_sentiment
from youtube import get_video_info
# import requests
from flask_cors import CORS
import matplotlib.pyplot as plt


app = Flask(__name__)
CORS(app)

def get_video(video_id):
    if not video_id:
        return {"error" : "video_id is required"}
    
    print("Get video",video_id)
    name, comments = get_video_info(video_id)
    predictions  = predict_sentiment(comments)

    positive = predictions.count("Positive")  
    negative = predictions.count("Negative")

    summary = {
        "name" : name,
        "positive" : positive,
        "negative" : negative,
        "num_comments" : len(comments),
        "rating" : round((positive/len(comments))*100, 2),
        # "data" : [positive,negative],
        # "labels" : ["positive","negative"]
    }

    return {"predictions" : predictions, "comments" : comments, "summary" : summary}


@app.route("/", methods=["GET","POST"])
def index():
    summary = None
    comments = []
    if request.method == "POST":
        video_url = request.form.get("video_url")
        video_id = video_url.split("v=")[1]
        data = get_video(video_id)
        
        summary = data['summary']
        comments = list(zip(data['comments'], data['predictions']))

    return render_template("index.html", summary = summary, comments = comments)

if __name__=="__main__":
    app.run(debug=True)