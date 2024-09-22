import json  # Import the json library
from flask import Flask, jsonify, request  # Ensure Flask is imported

app = Flask(__name__)

# Dummy emotion detection function (replace with your actual logic)
def emotion_detection_function(text):
    # Simulated response structure
    return {
        "anger": 0.1,
        "disgust": 0.0,
        "fear": 0.2,
        "joy": 0.5,
        "sadness": 0.2
    }

# Flask route for emotion detection
@app.route('/emotion-detect', methods=['POST'])
def emotion_detector():
    text_to_analyze = request.json.get('text')
    
    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    response = emotion_detection_function(text_to_analyze)
    
    emotions = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    if dominant_emotion is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    output = {
        **emotions,
        'dominant_emotion': dominant_emotion
    }
    
    return jsonify(output)

# For direct testing in the Python shell
def emotion_detector_with_text(text_to_analyze):
    response = emotion_detection_function(text_to_analyze)
    
    emotions = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    output = {
        **emotions,
        'dominant_emotion': dominant_emotion
    }
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
