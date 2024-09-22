import unittest
from emotion_detection.emotion_detection import emotion_detection_function

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }
        
        for statement, expected_emotion in test_cases.items():
            with self.subTest(statement=statement):
                result = emotion_detector_with_text(statement)
                print(f"Statement: {statement}, Result: {result}")  # Print the result
                self.assertEqual(result['dominant_emotion'], expected_emotion,
                                 f"Expected dominant emotion '{expected_emotion}' for '{statement}' but got '{result['dominant_emotion']}'")

if __name__ == '__main__':
    unittest.main()
