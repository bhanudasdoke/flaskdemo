"""Server module for emotion detection using Flask."""

from flask import Flask, jsonify, request
from emotion_detection import emotion_detector_with_text

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """Endpoint to analyze text for emotions."""
    text_to_analyze = request.json.get('text')

    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    result = emotion_detector_with_text(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
