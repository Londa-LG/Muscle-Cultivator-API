from fastapi import Depends,HTTPException,APIRouter
from schema import Workout
from models import Workout_Model

router = APIRouter(
    tags = ["Workout end-points"],
    prefix = "/workouts"
)

@router.post("/", response_model=Workout)
def create_workout(data: Workout):
    pass

@router.get("/",response_model=Workout)
def get_workouts():
    db = Workout_Model()
    return db.read_all()

@router.get("/{id}",response_model=Workout)
def get_workout(id: int):
    pass

@router.put("/{id}",response_model=Workout)
def update_workout(id: int,data: Workout):
    pass

@router.delete("/{id}")
def delete_user(id: int):
    pass
