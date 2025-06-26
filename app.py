from flask import Flask, request, jsonify
from textblob import TextBlob
import random

app = Flask(__name__)

# Sample responses
responses = {
    "positive": {
        "todos": ["Set a new goal", "Help a friend", "Reflect on achievements"],
        "tip": "Keep a gratitude journal today.",
        "quote": "Happiness is not something ready made. It comes from your own actions.",
        "video": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    },
    "negative": {
        "todos": ["Take a walk", "Write your thoughts", "Do a calming activity"],
        "tip": "Drink water and rest your eyes for 5 minutes.",
        "quote": "This too shall pass.",
        "video": "https://www.youtube.com/watch?v=ZToicYcHIOU"
    },
    "neutral": {
        "todos": ["Do something creative", "Organize your desk", "Listen to music"],
        "tip": "Breathe deeply for a minute.",
        "quote": "Every day may not be good... but there is something good in every day.",
        "video": "https://www.youtube.com/watch?v=oHv6vTKD6lg"
    }
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        mood = "positive"
    elif polarity < -0.1:
        mood = "negative"
    else:
        mood = "neutral"

    r = responses[mood]
    return jsonify({
        "emotion": mood,
        "todos": r["todos"],
        "tip": r["tip"],
        "quote": r["quote"],
        "video": r["video"]
    })

if __name__ == '__main__':
    app.run(debug=True)
