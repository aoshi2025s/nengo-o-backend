from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

import api.cruds.question as question_crud
from api.db import get_db

import api.schemas.question as question_schemas

router = APIRouter()

# GETでのリソース取得

@router.get("/questions",tags=["questions"], response_model = list[question_schemas.Question])
async def list_questions(db: Session = Depends(get_db)):
    return question_crud.get_question(db)

@router.get("/questions/{question_id}",tags=["questions"],response_model = question_schemas.Question)
async def get_question(question_id: int, db: Session = Depends(get_db)):
    db_question = question_crud.get_question_by_id(db, question_id)
    if db_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Question id:{question_id} not found"
            )
    return db_question

# CRUD処理

@router.post("/questions", tags=["questions"], response_model = question_schemas.QuestionCreateResponse,status_code=status.HTTP_201_CREATED)
async def create_question(question: question_schemas.QuestionCreate, db: Session = Depends(get_db)):
    return question_crud.create_question(db, question)

@router.put("/questions", tags=["questions"], response_model = question_schemas.Question,status_code=status.HTTP_200_OK)
async def update_question(question: question_schemas.Question, db: Session = Depends(get_db)):
    updated_question = question_crud.update_question(db, question.id, question)
    if updated_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Question id:{question.id} not found"
            )
    return updated_question

@router.delete("/questions/{question_id}", tags=["questions"], status_code=status.HTTP_200_OK)
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    delete_success = question_crud.delete_question(db, question_id)
    if not delete_success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Question id:{question_id} not found"
            )
    return {"message": "Question deleted successfully"}



