from typing import Dict,List
from pydantic import EmailStr, BaseModel

class Workout(BaseModel):
    id: int
    slug: str
    type: str
    split: str
    reps: Dict[str,int]
    sets: Dict[str,int]
    rest_time: float
    day: str
    date: str

class Exercise(BaseModel):
    id: int
    slug: str
    name: str
    technique: str

class User(BaseModel):
    id: int
    email: EmailStr
    username: str
    password: str
    workouts: List[int]
    awards: List[int]

class Rating(BaseModel):
    id: int
    level: int
    requirements: Dict[str,str]
    exercise: str
    details: str

class Progress(BaseModel):
    id: int
    slug: str
    user: int
    workout: List[int]

class Achievement(BaseModel):
    id: int
    slug: str
    name: str
    details: str
    requirements: Dict[str,str]

