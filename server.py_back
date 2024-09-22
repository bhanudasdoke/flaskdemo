import json
from flask import Flask, jsonify, request, render_template
from emotion_detection import emotion_detector_with_text

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    # Get the text from the request
    text_to_analyze = request.json.get('text')
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    # Call the emotion detection function
    response = emotion_detector_with_text(text_to_analyze)
    
    # Prepare the output format
    output = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }
    
    # Create the formatted response string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {output['anger']}, 'disgust': {output['disgust']}, "
        f"'fear': {output['fear']}, 'joy': {output['joy']} and "
        f"'sadness': {output['sadness']}. The dominant emotion is {output['dominant_emotion']}."
    )
    
    # Return the output as JSON
    return jsonify(formatted_response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
