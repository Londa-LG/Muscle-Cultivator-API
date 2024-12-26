from typing import List
from connect import get_db
from models import Rating_Model
from sqlalchemy.orm import Session
from schema import Rating, Rating_Response
from utils import dict_to_string, string_to_dict
from fastapi import Depends,HTTPException,APIRouter, status, Response

router = APIRouter(
    tags = ["Ratings end-points"],
    prefix = "/ratings"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Rating_Response)
def create_rating(data: Rating,db: Session = Depends(get_db)):
    data.requirements = dict_to_string(data.requirements)

    new_rating = Rating_Model(**data.dict())
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)

    new_rating.requirements = string_to_dict(new_rating.requirements)

    return new_rating
    

@router.get("/", response_model=List[Rating_Response])
def get_ratings(db: Session = Depends(get_db)):
    ratings = db.query(Rating_Model).all()

    if not ratings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No ratings found")

    for rating in ratings:
        rating.requirements = string_to_dict(rating.requirements)

    return ratings

@router.get("/{id}", response_model=Rating_Response)
def get_rating(id: int,db: Session = Depends(get_db)):
    rating = db.query(Rating_Model).filter(Rating_Model.id == id).first()

    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No rating with that id found")

    rating.requirements = string_to_dict(rating.requirements)

    return rating

@router.put("/{id}", response_model=Rating_Response)
def update_rating(id: int,data: Rating,db: Session = Depends(get_db)):
    rating = db.query(Rating_Model).filter(Rating_Model.id == id)

    if not rating.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No rating with that id found")

    data.requirements = dict_to_string(data.requirements)

    rating.update(data.dict())
    db.commit()

    rating = rating.first()
    rating.requirements = string_to_dict(rating.requirements)

    return rating

@router.delete("/{id}", response_model=Rating_Response)
def delete_rating(id: int,db: Session = Depends(get_db)):
    rating = db.query(Rating_Model).filter(Rating_Model.id == id)

    if not rating.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No rating with that id found")

    rating.delete()
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
