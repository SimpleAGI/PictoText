import unittest
from src.main import extract_text, analyze_sentiment

class TestPictoText(unittest.TestCase):
    def test_extract_text(self):
        # Placeholder for actual image path
        pass

    def test_analyze_sentiment(self):
        text = "I love sunny days"
        sentiment = analyze_sentiment(text)
        self.assertGreater(sentiment.polarity, 0)

if __name__ == '__main__':
    unittest.main()