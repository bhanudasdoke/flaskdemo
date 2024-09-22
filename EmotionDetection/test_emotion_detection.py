import unittest
from emotion_detection.emotion_detection import emotion_detection_function

class TestEmotionDetection(unittest.TestCase):
    
    def setUp(self):
        # This method will run before each test
        self.test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

    def test_emotion_detection(self):
        for statement, expected_emotion in self.test_cases.items():
            with self.subTest(statement=statement):
                result = emotion_detection_function(statement)
                dominant_emotion = max(result, key=result.get)  # Get the emotion with the highest score
                self.assertEqual(dominant_emotion, expected_emotion, 
                                 f"Expected dominant emotion '{expected_emotion}' for '{statement}' but got '{dominant_emotion}'")

if __name__ == '__main__':
    unittest.main()

