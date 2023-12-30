from fastapi import APIRouter

import api.schemas.question as question_schemas

router = APIRouter()

@router.get("/questions",tags=["questions"], response_model = list[question_schemas.Question])
async def list_questions():
    return [question_schemas.Question(id=1, question_sentense="ビザンツ帝国が滅亡", question_answer="1453")]

@router.get("/questions/{question_id}",tags=["questions"],response_model = question_schemas.Question)
async def get_question(question_id: int):
    return question_schemas.Question(id=1, question_sentense="ビザンツ帝国が滅亡", question_answer="1453")

@router.post("/questions", tags=["questions"], response_model = question_schemas.QuestionCreateResponse)
async def create_question(question: question_schemas.QuestionCreate):
    return question_schemas.QuestionCreateResponse(id=2, question_sentense=question.question_sentense, question_answer=question.question_answer)

@router.put("/questions", tags=["questions"], response_model = question_schemas.Question)
async def update_question(question: question_schemas.Question):
    return question

@router.delete("/questions/{question_id}", tags=["questions"])
async def delete_question(question_id: int):
    return {"message": "deleted"}



