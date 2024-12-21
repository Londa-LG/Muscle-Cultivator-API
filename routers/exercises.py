from fastapi import Depends,HTTPException,APIRouter

router = APIRouter(
    tags = ["Exercises end-points"],
    prefix = "/exercises"
)
