from typing import List
from connect import get_db
from models import Workout_Model
from sqlalchemy.orm import Session
from schema import Workout, Workout_Response
from fastapi import Depends,HTTPException,APIRouter, status, Response
from utils import dict_to_string, list_to_string, string_to_list, string_to_dict

router = APIRouter(
    tags = ["Workout end-points"],
    prefix = "/workouts"
)

@router.post("/", response_model=Workout)
def create_workout(data: Workout,db: Session = Depends(get_db)):
    original = data
    data.exercises = list_to_string(data.exercises)
    data.reps = dict_to_string(data.reps)
    data.sets = dict_to_string(data.sets)
    
    new_workout = Workout_Model(**data.dict())
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)

    return original

@router.get("/", response_model=List[Workout_Response])
def get_workouts(db: Session = Depends(get_db)):
    workouts = db.query(Workout_Model).all()

    if not workouts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No workouts found")

    for workout in workouts:
        workout.exercises = string_to_list(workout.exercises)
        workout.reps = string_to_dict(workout.reps)
        workout.sets = string_to_dict(workout.sets)

    return workouts
    

@router.get("/{id}",response_model=Workout_Response)
def get_workout(id: int,db: Session = Depends(get_db)):
    workout = db.query(Workout_Model).filter(Workout_Model.id == id).first()

    if not workout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No workout with that id found")

    workout.exercises = string_to_list(workout.exercises)
    workout.reps = string_to_dict(workout.reps)
    workout.sets = string_to_dict(workout.sets)

    return workout

@router.put("/{id}",response_model=Workout_Response)
def update_workout(id: int,data: Workout,db: Session = Depends(get_db)):
    workout = db.query(Workout_Model).filter(Workout_Model.id == id)

    if not workout.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No workout with that id found")

    data.exercises = list_to_string(data.exercises)
    data.reps = dict_to_string(data.reps)
    data.sets = dict_to_string(data.sets)

    workout.update(data.dict())
    db.commit()

    workout = workout.first()
    workout.exercises = string_to_list(workout.exercises)
    workout.reps = string_to_dict(workout.reps)
    workout.sets = string_to_dict(workout.sets)

    return workout

@router.delete("/{id}")
def delete_workout(id: int,db: Session = Depends(get_db)):
    workout = db.query(Workout_Model).filter(Workout_Model.id == id)

    if not workout.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No workout with that id found")

    workout.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
