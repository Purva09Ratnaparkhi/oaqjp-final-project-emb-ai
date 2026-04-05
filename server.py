from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("textToAnalyze")

    # Error handling (Task 7)
    if not text:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    response = f"""
    For the given statement, the system response is:
    anger: {result['anger']},
    disgust: {result['disgust']},
    fear: {result['fear']},
    joy: {result['joy']},
    sadness: {result['sadness']}.
    The dominant emotion is {result['dominant_emotion']}.
    """

    return response

if __name__ == "__main__":
    app.run(debug=True)