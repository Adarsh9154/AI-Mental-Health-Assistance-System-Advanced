import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

fallback_responses = {
    "sadness": "I'm here for you. Try taking some rest and talking to someone you trust.",

    "joy": "That's wonderful to hear! Keep doing what makes you happy.",

    "anger": "Take a deep breath. Try relaxing for a few minutes.",

    "fear": "Everything will be okay. Focus on one step at a time.",

    "neutral": "Thank you for sharing your thoughts with me."
}


def generate_response(emotion, user_text):

    prompt = f"""
    You are a supportive AI mental health assistant.

    User emotion: {emotion}

    User message: {user_text}

    Provide:
    - empathetic response
    - emotional support
    - coping suggestion

    Keep response short and supportive.
    """

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print("✅ GROQ AI Running")

        return response.choices[0].message.content

    except Exception as e:

        print("❌ GROQ Failed")
        print("Error:", e)

        return fallback_responses.get(
            emotion,
            "I'm always here to support you."
        )