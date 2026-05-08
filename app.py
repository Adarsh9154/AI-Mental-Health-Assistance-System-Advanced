import streamlit as st
from streamlit_chat import message

from models.emotion_model import detect_emotion
from chatbot.response_generator import generate_response
from utils.suggestions import get_suggestions

from dashboard.charts import load_data
from dashboard.charts import emotion_chart

from database.db import Session
from database.db import MoodLog

from voice.transcriber import transcribe_audio

from streamlit_mic_recorder import mic_recorder


st.set_page_config(
    page_title="AI Mental Health Assistant",
    layout="centered"
)

st.title("AI Mental Health Assistant")

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Chat Assistant",
        "Dashboard",
        "About"
    ]
)


# =========================
# CHAT ASSISTANT PAGE
# =========================

if page == "Chat Assistant":
        # Chat History Memory

    if "messages" not in st.session_state:

        st.session_state.messages = []

    st.write(
        "Talk with the AI assistant using text or microphone input."
    )

    # Initialize input
    user_input = ""

    # Text Input
    text_input = st.text_area(
        "Type your thoughts here"
    )

    if text_input:

        user_input = text_input

    st.markdown("---")

    st.subheader("Voice Input")

    # Microphone Recorder
    audio = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording",
        just_once=True
    )

    # Speech-to-text
    if audio:

        with open("temp_audio.wav", "wb") as f:

            f.write(audio["bytes"])

        st.audio(audio["bytes"])

        transcribed_text = transcribe_audio(
            "temp_audio.wav"
        )

        st.subheader("Transcribed Text")

        st.write(transcribed_text)

        # Use voice text as input
        user_input = transcribed_text

    # Analyze Emotion
    if st.button("Analyze Emotion"):

        if user_input.strip() == "":

            st.warning(
                "Please enter or record something."
            )

        else:

            # Emotion Detection
            emotion, score = detect_emotion(
                user_input
            )

            # AI Response
            with st.spinner("AI is analyzing your emotions..."):

                response = generate_response(
                emotion,
                user_input
            )

            # Suggestions
            suggestions = get_suggestions(
                emotion
            )

            # Store in Database
            session = Session()

            mood = MoodLog(
                text=user_input,
                emotion=emotion
            )

            session.add(mood)
            session.commit()

            # Chat UI
            # Store chat messages

            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"""
Emotion Detected: {emotion}

Confidence Score: {score:.2f}

AI Response:

{response}
"""
            })

             # Suggestions
            st.subheader("Suggestions")

            for s in suggestions:

                st.write("-", s)

            st.markdown("---")

            # Display Chat History

            for idx, msg in enumerate(
                st.session_state.messages
            ):

                if msg["role"] == "user":

                    message(
                        msg["content"],
                        is_user=True,
                        key=f"user_{idx}"
                    )

                else:

                    message(
                        msg["content"],
                        key=f"assistant_{idx}"
                    )


# =========================
# DASHBOARD PAGE
# =========================

if page == "Dashboard":

    st.header("Mood Analytics Dashboard")

    df = load_data()

    if not df.empty:

        st.subheader("Mood History")

        st.dataframe(df)

        st.subheader("Emotion Frequency")

        fig = emotion_chart(df)

        st.plotly_chart(fig)

    else:

        st.info(
            "No mood data available yet."
        )


# =========================
# ABOUT PAGE
# =========================

if page == "About":

    st.header("About This Project")

    st.write("""
This AI Mental Health Assistant is a multimodal AI application.

Technologies Used:

- HuggingFace Transformers
- Groq Llama 3
- Whisper Speech-to-Text
- Streamlit
- SQLite
- Plotly

Features:

- Emotion Detection
- AI-generated Responses
- Voice Input Support
- Text Chat Support
- Mood Analytics Dashboard
- Speech-to-Text Processing
""")