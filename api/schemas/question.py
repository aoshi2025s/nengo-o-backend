from pydantic import BaseModel, Field

class QuestionBase(BaseModel):
    question_sentense: str
    question_answer: str

class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

class QuestionCreate(QuestionBase):
    pass

class QuestionCreateResponse(QuestionBase):
    id: int

    class Config:
        orm_mode = True

