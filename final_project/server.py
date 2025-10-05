"""Flask web server for Emotion Detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze emotions from the input text using the emotion_detector function.

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the index.html page for user input.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
