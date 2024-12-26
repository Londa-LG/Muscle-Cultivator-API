from typing import Dict,List, Optional
from pydantic import EmailStr, BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]

class Workout(BaseModel):
    slug: str
    type: str
    exercises: List[str]
    split: str
    reps: Dict[str,int]
    sets: Dict[str,int]
    rest_time: float
    day: str
    date: str

class Workout_Response(Workout):
    id: int

class Exercise(BaseModel):
    slug: str
    name: str
    technique: str

class Exercise_Response(Exercise):
    id: int

class User(BaseModel):
    email: EmailStr
    username: str
    password: str
    workouts: List[int]
    awards: List[int]

class User_Response(User):
    id: int

class Rating(BaseModel):
    level: int
    requirements: Dict[str,str]
    exercise: str
    details: str

class Rating_Response(Rating):
    id: int

class Progress(BaseModel):
    slug: str
    user: int
    workouts: List[int]

class Progress_Response(Progress):
    id: int

class Achievement(BaseModel):
    slug: str
    name: str
    details: str
    requirements: Dict[str,str]

class Achievement_Response(Achievement):
    id: int
