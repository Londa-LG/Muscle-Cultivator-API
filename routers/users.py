from schema import User
from fastapi import Depends,HTTPException,APIRouter,status

router = APIRouter(
    tags = ["Users end-points"],
    prefix = "/users"
)

@router.post("/", status_code = status.HTTP_201_CREATED,response_model=User)
def create_user(data: User):
    pass

@router.get("/{id}", response_model=User)
def get_user(id: int):
    pass

@router.put("/{id}", response_model=User)
def update_user(id: int):
    pass

@router.delete("/{id}", response_model=User)
def delete_user(id: int):
    pass
