from typing import List
from connect import get_db
from models import Exercise_Model
from sqlalchemy.orm import Session
from schema import Exercise, Exercise_Response
from fastapi import Depends,HTTPException,APIRouter, status, Response

router = APIRouter(
    tags = ["Exercises end-points"],
    prefix = "/exercises"
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Exercise_Response)
def create_exercise(data: Exercise,db: Session = Depends(get_db)):
    new_exercise = Exercise_Model(**data.dict())
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)

    return new_exercise
    

@router.get("/", response_model=List[Exercise_Response])
def get_exercises(db: Session = Depends(get_db)):
    exercises = db.query(Exercise_Model).all()

    if not exercises:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No exercises found")

    return exercises

@router.get("/{id}", response_model=Exercise_Response)
def get_exercise(id: int,db: Session = Depends(get_db)):
    exercise = db.query(Exercise_Model).filter(Exercise_Model.id == id).first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No exercise with that id found")

    return exercise

@router.put("/{id}", response_model=Exercise_Response)
def update_exercise(id: int,data: Exercise,db: Session = Depends(get_db)):
    exercise = db.query(Exercise_Model).filter(Exercise_Model.id == id)

    if not exercise.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No exercise with that id found")

    exercise.update(data.dict())
    db.commit()

    return exercise.first()
@router.delete("/{id}", response_model=Exercise_Response)
def delete_exercise(id: int,db: Session = Depends(get_db)):
    exercise = db.query(Exercise_Model).filter(Exercise_Model.id == id)

    if not exercise.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No exercise with that id found")

    exercise.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
