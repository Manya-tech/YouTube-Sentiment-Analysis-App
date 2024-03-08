import streamlit as st
from predict import predict_sentiment
from youtube import get_video_info
import pandas as pd


def get_video(video_id):
    if not video_id:
        return {"error" : "video_id is required"}
    
    print("get video",video_id)
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

    return summary

def main():
    st.set_page_config(page_title="HateLoveHue", page_icon=":guardsman:", layout="wide")
    st.title("HateLoveHue: YouTube Video Sentiment Analysis")
    st.subheader("Enter YouTube Video Links")

    videoLinks = st.text_area("YouTube Video Link", "Paste video links here, separated by a ,")
    video_links = videoLinks.split(",")
    if st.button("Generate Report"):
        
        try:
            for video_link in video_links:
                video_id = video_link.split("v=")[1]
                res = get_video(video_id)
                positive = res['positive']
                negative=res['negative']
                rating = res['rating']
                st.header(res['name'],divider='rainbow')
                st.subheader("Sentiment Analysis Report")
                st.write(f"Total Comments: {res['num_comments']}")
                st.write(f"Positive Comments: {positive}")
                st.write(f"Negative Comments: {negative}")
                st.write(f"Rating: {rating}%")
                st.subheader("Sentiment Analysis Distribution")
                data = pd.DataFrame({"num" :[positive,negative], "labels":["Positive", "Negative"]})
                data = data.set_index("labels")
                st.bar_chart(data)
            
        except Exception as e:
            st.write(f"Error processing {video_links}: {e}")


if __name__ == "__main__":
    main()