from schema import Progress
from fastapi import Depends,HTTPException,APIRouter, status

router = APIRouter(
    tags = ["Progress end-points"],
    prefix = "/progress"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Progress)
def create_progress(data: Progress):
    pass

@router.get("/", response_model=Progress)
def get_progress():
    pass

@router.get("/{id}", response_model=Progress)
def get_progress(id: int):
    pass

@router.put("/{id}", response_model=Progress)
def update_progress(id: int):
    pass

@router.delete("/{id}", response_model=Progress)
def delete_progress(id: int):
    pass
