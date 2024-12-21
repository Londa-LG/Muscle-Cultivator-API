from fastapi import Depends,HTTPException,APIRouter
from schema import Workout

router = APIRouter(
    tags = ["Workout end-points"],
    prefix = "/workouts"
)

@router.post("/", response_model=Workout)
def create_workout(data: Workout):
    pass

@router.get("/",response_model=Workout)
def get_posts():
    pass

@router.get("/{id}",response_model=Workout)
def get_post(id: int):
    pass

@router.put("/{id}",response_model=Workout)
def update_workout(id: int,data: Workout):
    pass

@router.delete("/{id}")
def delete_user(id: int):
    pass
