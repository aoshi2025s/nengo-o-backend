from sqlalchemy.orm import Session
from sqlalchemy import select

import api.models.question as question_model
import api.schemas.question as question_schema

def get_question(db: Session) -> list[question_model.Question]:
    return db.query(question_model.Question).all()

def get_question_by_id(db: Session, question_id: int) -> question_model.Question:
    return db.query(question_model.Question).filter(question_model.Question.id == question_id).first()

def create_question(db: Session, question_create: question_schema.QuestionCreate) -> question_model.Question:
    question = question_model.Question(question_sentense=question_create.question_sentense, question_answer=question_create.question_answer)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

# question_idを指定して、questionを更新する
def update_question(db: Session, question_id: int, question_update: question_schema.Question) -> question_model.Question:
    db_question = db.query(question_model.Question).filter(question_model.Question.id == question_id).first()
    db_question.question_sentense = question_update.question_sentense
    db_question.question_answer = question_update.question_answer
    db.commit()
    db.refresh(db_question)
    return db_question

# question_idを指定して、questionを削除する
def delete_question(db: Session, question_id: int):
    db_question = db.query(question_model.Question).filter(question_model.Question.id == question_id).first()
    if db_question is None:
        return None
    else:
        db.delete(db_question)
        db.commit()
        return True