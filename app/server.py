from flask import Flask, request, render_template
from predict import predict_sentiment
from youtube import get_video_comments
from flask_cors import CORS