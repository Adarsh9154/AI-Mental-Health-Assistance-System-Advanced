import os

import whisper


# Add FFmpeg path
os.environ["PATH"] += os.pathsep + r"C:\Users\Adarsh\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

model = whisper.load_model("base")


def transcribe_audio(audio_path):

    result = model.transcribe(audio_path)

    return result["text"]