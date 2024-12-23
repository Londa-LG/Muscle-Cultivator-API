from schema import Rating
from fastapi import Depends,HTTPException,APIRouter, status

router = APIRouter(
    tags = ["Ratings end-points"],
    prefix = "/ratings"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Rating)
def create_rating(data: Rating):
    pass

@router.get("/", response_model=Rating)
def get_ratings():
    pass

@router.get("/{id}", response_model=Rating)
def get_rating(id: int):
    pass

@router.put("/{id}}", response_model=Rating)
def update_rating(id: int):
    pass

@router.delete("/{id}}", response_model=Rating)
def delete_rating(id: int):
    pass
