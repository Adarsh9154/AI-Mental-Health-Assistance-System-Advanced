# AI Mental Health Assistant

An AI-powered multimodal mental wellness assistant that understands human emotions through text and voice interaction and provides intelligent emotional support using modern AI technologies.

---

## Overview

AI Mental Health Assistant is an interactive AI application designed to support mental wellness through emotionally aware conversations. The system combines Natural Language Processing (NLP), Large Language Models (LLMs), Speech-to-Text technology, and analytics to create a smart and user-friendly mental health support platform.

Users can communicate with the assistant either by typing messages or speaking through a microphone. The application analyzes emotional states from user input and generates empathetic AI-driven responses along with personalized wellness suggestions.

The project also includes a mood analytics dashboard that tracks emotional trends and conversation history for a more engaging and insightful experience.

---

## Features

* Emotion Detection using HuggingFace Transformers
* AI-generated Emotional Support using Groq Llama 3
* Voice and Text Interaction
* Speech-to-Text using OpenAI Whisper
* Real-time Microphone Input
* Conversation History Memory
* Mood Analytics Dashboard
* Interactive Chat-style Interface
* SQLite Database Integration
* Personalized Wellness Suggestions

---

## Technologies Used

| Technology               | Purpose                   |
| ------------------------ | ------------------------- |
| Python                   | Core Programming Language |
| Streamlit                | Frontend Web Application  |
| HuggingFace Transformers | Emotion Detection         |
| Groq Llama 3             | AI Response Generation    |
| OpenAI Whisper           | Speech-to-Text            |
| SQLite                   | Database                  |
| SQLAlchemy               | Database ORM              |
| Plotly                   | Analytics Dashboard       |

---

## Project Architecture

```bash id="t4e9a2"
User Input (Text / Voice)
            │
            ▼
Speech-to-Text (Whisper)
            │
            ▼
Emotion Detection (Transformers)
            │
            ▼
AI Response Generation (Llama 3)
            │
            ▼
Suggestions + Mood Analytics
            │
            ▼
SQLite Database Storage
```

---

## Project Structure

```bash id="u6r8k1"
AI_Mental_Health_Assistant/
│
├── app.py
├── requirements.txt
│
├── chatbot/
│   └── response_generator.py
│
├── models/
│   └── emotion_model.py
│
├── voice/
│   └── transcriber.py
│
├── utils/
│   └── suggestions.py
│
├── dashboard/
│   └── charts.py
│
├── database/
│   └── db.py
│
└── database.db
```

---

## Installation

### Clone Repository

```bash id="j8l2n4"
git clone https://github.com/your-username/AI-Mental-Health-Assistant.git
```

### Navigate to Project Folder

```bash id="x1z7m5"
cd AI-Mental-Health-Assistant
```

### Create Virtual Environment

```bash id="p0d8q3"
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash id="g7h4s2"
venv\Scripts\activate
```

#### Linux / Mac

```bash id="f2a5v9"
source venv/bin/activate
```

### Install Dependencies

```bash id="k6m1b8"
pip install -r requirements.txt
```

---

## Run Application

```bash id="c5r9t1"
streamlit run app.py
```

---

## Key Functionalities

### Emotion Detection

Detects emotions such as stress, anxiety, sadness, fear, anger, joy, and neutral emotions using transformer-based NLP models.

### AI-generated Support

Generates empathetic and emotionally aware responses using Groq Llama 3.

### Voice Interaction

Supports real-time microphone interaction and speech-to-text conversion using Whisper.

### Mood Analytics

Tracks emotional trends and visualizes mood history through interactive dashboards.

### Conversation Memory

Maintains session-based chat history for a realistic conversational AI experience.

---

## Future Enhancements

* AI Voice Reply
* Personalized Mental Health Reports
* Real-time Emotion Monitoring
* User Authentication System
* Cloud Deployment
* Fine-tuned Emotion Classification Models

---

## Objective

The objective of this project is to develop an intelligent AI-based mental health assistant capable of understanding emotions and providing supportive conversational assistance through multimodal interaction.

---

## License

This project is licensed under the MIT License.
