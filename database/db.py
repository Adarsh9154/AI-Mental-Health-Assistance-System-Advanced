from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime


engine = create_engine("sqlite:///database.db")

Base = declarative_base()


class MoodLog(Base):

    __tablename__ = "mood_logs"

    id = Column(Integer, primary_key=True)

    text = Column(String)

    emotion = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)