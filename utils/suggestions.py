suggestions = {
    "sadness": [
        "Listen to calming music",
        "Talk to a friend",
        "Write your feelings in a journal"
    ],

    "anger": [
        "Try breathing exercises",
        "Take a short walk",
        "Listen to relaxing sounds"
    ],

    "fear": [
        "Practice meditation",
        "Focus on positive thoughts",
        "Try grounding exercises"
    ],

    "joy": [
        "Share your happiness with others",
        "Keep a gratitude journal"
    ]
}

def get_suggestions(emotion):
    return suggestions.get(
        emotion,
        ["Take care of yourself"]
    )