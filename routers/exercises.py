from schema import Exercise
from fastapi import Depends,HTTPException,APIRouter, status

router = APIRouter(
    tags = ["Exercises end-points"],
    prefix = "/exercises"
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Exercise)
def create_exercise(data: Exercise):
    pass

@router.get("/", response_model=Exercise)
def get_exercises():
    pass

@router.get("/{id}", response_model=Exercise)
def get_exercise(id: int):
    pass

@router.put("/{id}", response_model=Exercise)
def update_exercise(id: int):
    pass

@router.delete("/{id}", response_model=Exercise)
def delete_exercise(id: int):
    pass
