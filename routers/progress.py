from fastapi import Depends,HTTPException,APIRouter

router = APIRouter(
    tags = ["Progress end-points"],
    prefix = "/progress"
)
