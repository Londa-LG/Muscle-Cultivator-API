from fastapi import Depends,HTTPException,APIRouter, status
from schema import Achievement,User

router = APIRouter(
    tags = ["Achievements end-points"],
    prefix = "/achievements"
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Achievement)
def create_achievement(data: Achievement):
    pass

@router.get("/", response_model=Achievement)
def get_achievements():
    pass


@router.get("/{id}", response_model=Achievement)
def get_achievement(id: int):
    pass

@router.put("/{id}", response_model=Achievement)
def update_achievement(id: int):
    pass

@router.delete("/{id}")
def delte_achievement(id: int):
    pass
