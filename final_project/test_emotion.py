"""Simple runner to test the emotion_detector function."""
from .EmotionDetection.emotion_detection import emotion_detector


def main():
    text = "I love this new technology."
    result = emotion_detector(text)
    print("Input:", text)
    print("Output:", result)


if __name__ == "__main__":
    main()
