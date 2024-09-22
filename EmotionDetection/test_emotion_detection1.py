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

    # Normalize scores (optional, depending on your use case)
    total_score = sum(emotions.values())
    if total_score > 0:
        for emotion in emotions:
            emotions[emotion] /= total_score  # Normalize to sum to 1

    return emotions
