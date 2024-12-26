from models import Base
from connect import engine
from fastapi import FastAPI
from routers import users,workouts,exercises,achievements,ratings,progress

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(workouts.router)
app.include_router(exercises.router)
app.include_router(ratings.router)
app.include_router(progress.router)
app.include_router(achievements.router)
