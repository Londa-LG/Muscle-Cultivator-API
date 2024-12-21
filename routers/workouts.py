from schema import Workout
from fastapi import Depends,HTTPException,APIRouter

router = APIRouter(
    tags = ["Workout end-points"],
    prefix = "/workouts"
)

