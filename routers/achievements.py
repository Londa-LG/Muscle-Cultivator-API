from fastapi import Depends,HTTPException,APIRouter

router = APIRouter(
    tags = ["Achievements end-points"],
    prefix = "/achievements"
)
