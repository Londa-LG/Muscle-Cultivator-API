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

    new_ach.requirements = dict_to_string(new_ach.requirements)

    return new_ach


@router.get("/", response_model=Achievement)
def get_achievements():
    pass


@router.get("/{id}", response_model=Achievement)
def get_achievement(id: int):
    pass

@router.put("/{id}", response_model=Achievement)
def update_achievement(id: int):
    pass

@router.delete("/{id}")
def delte_achievement(id: int):
    pass
