from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_sentense = Column(String(1024))
    question_answer = Column(String(255))