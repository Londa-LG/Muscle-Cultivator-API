from typing import List
from connect import get_db
from models import Progress_Model
from sqlalchemy.orm import Session
from schema import Progress, Progress_Response
from utils import string_to_list, list_to_string
from fastapi import Depends,HTTPException,APIRouter, status, Response

router = APIRouter(
    tags = ["Progress end-points"],
    prefix = "/progress"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Progress_Response)
def create_progress(data: Progress,db: Session = Depends(get_db)):
    data.workouts = list_to_string(data.workouts)
    
    new_progress = Progress_Model(**data.dict())
    db.add(new_progress)
    db.commit()
    db.refresh(new_progress)

    new_progress.workouts = string_to_list(new_progress.workouts)

    return new_progress

@router.get("/", response_model=List[Progress_Response])
def get_progress(db: Session = Depends(get_db)):
    progress = db.query(Progress_Model).all()

    if not progress:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No progress with that id found")

    for prog in progress:
        prog.workouts = string_to_list(prog.workouts)

    return progress

@router.get("/{id}", response_model=Progress_Response)
def get_progress(id: int,db: Session = Depends(get_db)):
    progress = db.query(Progress_Model).filter(Progress_Model.id == id).first()

    if not progress:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No progress with that id found")

    progress.workouts = string_to_list(progress.workouts)

    return progress

@router.put("/{id}", response_model=Progress_Response)
def update_progress(id: int,data: Progress,db: Session = Depends(get_db)):
    progress = db.query(Progress_Model).filter(Progress_Model.id == id)

    if not progress.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No progress with that id found")

    data.workouts = list_to_string(data.workouts)

    progress.update(data.dict())
    db.commit()

    progress = progress.first()
    progress.workouts = string_to_list(progress.workouts)

    return progress


@router.delete("/{id}")
def delete_progress(id: int,db: Session = Depends(get_db)):
    progress = db.query(Progress_Model).filter(Progress_Model.id == id)

    if not progress.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No progress with that id found")

    progress.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

