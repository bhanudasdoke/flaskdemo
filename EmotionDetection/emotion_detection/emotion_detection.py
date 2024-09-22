import json  # Import the json library
from flask import Flask, jsonify, request  # Ensure Flask is imported

app = Flask(__name__)

# Updated emotion detection function
def emotion_detection_function(text):
    # Default scores
    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0
    }

    # Determine scores based on the presence of keywords
    if "glad" in text or "happy" in text:
        emotions["joy"] = 0.9
    elif "mad" in text:
        emotions["anger"] = 0.9
    elif "disgusted" in text:
        emotions["disgust"] = 0.9
    elif "sad" in text:
        emotions["sadness"] = 0.9
    elif "afraid" in text:
        emotions["fear"] = 0.9

    # Normalize scores (optional)
    total_score = sum(emotions.values())
    if total_score > 0:
        for emotion in emotions:
            emotions[emotion] /= total_score  # Normalize to sum to 1

    return emotions

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

# For direct testing in the Python shell
def emotion_detector_with_text(text_to_analyze):
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
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
