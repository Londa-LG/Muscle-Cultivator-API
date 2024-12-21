from fastapi import Depends,HTTPException,APIRouter

router = APIRouter(
    tags = ["Ratings end-points"],
    prefix = "/ratings"
)
