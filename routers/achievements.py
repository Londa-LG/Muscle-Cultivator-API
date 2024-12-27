from typing import List
from connect import get_db
from sqlalchemy.orm import Session
from models import Achievements_Model
from utils import dict_to_string, string_to_dict
from schema import Achievement, Achievement_Response
from fastapi import Depends,HTTPException,APIRouter, status, Response

router = APIRouter(
    tags = ["Achievements end-points"],
    prefix = "/achievements"
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Achievement_Response)
def create_achievement(data: Achievement,db: Session = Depends(get_db)):
    data.requirements = dict_to_string(data.requirements)

    new_ach = Achievements_Model(**data.dict())
    db.add(new_ach)
    db.commit()
    db.refresh(new_ach)

    new_ach.requirements = string_to_dict(new_ach.requirements)

    return new_ach


@router.get("/", response_model=List[Achievement_Response])
def get_achievements(db: Session = Depends(get_db)):
    achs = db.query(Achievements_Model).all()

    if not achs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No achievements found")

    for ach in achs:
        ach.requirements = string_to_dict(ach.requirements)

    return achs

@router.get("/{id}", response_model=Achievement)
def get_achievement(id: int,db: Session = Depends(get_db)):
    ach = db.query(Achievements_Model).filter(Achievements_Model.id == id).first()

    if not ach:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No achievement with that id found")

    ach.requirements = string_to_dict(ach.requirements)

    return ach

@router.put("/{id}", response_model=Achievement_Response)
def update_achievement(id: int,data: Achievement,db: Session = Depends(get_db)):
    data.requirements = dict_to_string(data.requirements)
    ach = db.query(Achievements_Model).filter(Achievements_Model.id == id)

    if not ach.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No achievement with that id found")

    ach.update(data.dict())
    db.commit()

    ach = ach.first()
    ach.requirements = string_to_dict(ach.requirements)

    return ach

@router.delete("/{id}")
def delte_achievement(id: int,db: Session = Depends(get_db)):
    ach = db.query(Achievements_Model).filter(Achievements_Model.id == id)

    if not ach.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No achievement with that id found")

    ach.delete()
    db.commit()

    return Response(status_code = status.HTTP_204_NO_CONTENT)
