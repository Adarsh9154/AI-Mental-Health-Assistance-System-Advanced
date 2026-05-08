from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)


def map_emotion(emotion, text):

    text = text.lower()

    # Stress & anxiety keywords
    stress_words = [
        "stress",
        "stressed",
        "anxious",
        "anxiety",
        "pressure",
        "worried",
        "overthinking"
    ]

    if any(word in text for word in stress_words):

        return "stress/anxiety"

    # Default mapping
    return emotion


def detect_emotion(text):

    result = classifier(text)

    emotion = result[0][0]['label']
    score = result[0][0]['score']

    emotion = map_emotion(emotion, text)

    return emotion, score