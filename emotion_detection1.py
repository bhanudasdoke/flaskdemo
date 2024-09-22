from flask import Flask, jsonify, request
import json  # Import the json library
import requests  # Make sure you have this installed

app = Flask(__name__)

# Dummy emotion detection function (replace with your actual logic)
def emotion_detection_function(text):
    # Simulated response structure
    # Replace this with the actual API response when implementing
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
    # Get the text from the request
    text_to_analyze = request.json.get('text')
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    # Call the emotion detection function
    response = emotion_detection_function(text_to_analyze)
    
    # Convert the response to a dictionary
    emotions = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Prepare the final output
    output = {
        **emotions,
        'dominant_emotion': dominant_emotion
    }
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
