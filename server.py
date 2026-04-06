"""Flask server for Emotion Detection application."""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze text and return detected emotions."""
    text = request.args.get("textToAnalyze")

    if not text:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    response = (
        f"For the given statement, the system response is: "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(debug=True)
