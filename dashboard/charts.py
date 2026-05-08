import pandas as pd
import plotly.express as px

from database.db import Session
from database.db import MoodLog


def load_data():

    session = Session()

    data = session.query(MoodLog).all()

    moods = []

    for row in data:

        moods.append({
            "text": row.text,
            "emotion": row.emotion,
            "created_at": row.created_at
        })

    df = pd.DataFrame(moods)

    return df


def emotion_chart(df):

    fig = px.histogram(
        df,
        x="emotion",
        title="Emotion Frequency",
        text_auto=True
    )

    return fig