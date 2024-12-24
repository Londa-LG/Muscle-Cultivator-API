from fastapi import FastAPI
from models import Model
from routers import users,workouts,exercises,achievements,ratings

#model = Model("app.db")

app = FastAPI()

app.include_router(users.router)
app.include_router(workouts.router)
app.include_router(exercises.router)
app.include_router(achievements.router)
app.include_router(ratings.router)
