import cv2
import pytesseract
from textblob import TextBlob

# Function to extract text from image
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PictoText - Image to Text Converter with Sentiment Analysis")
    parser.add_argument('--image_path', type=str, required=True, help='Path to the image file')
    args = parser.parse_args()

    text = extract_text(args.image_path)
    print("Extracted Text:", text)

    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)
