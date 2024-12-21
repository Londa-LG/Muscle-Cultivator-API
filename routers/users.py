from fastapi import Depends,HTTPException,APIRouter,status

router = APIRouter(
    tags = ["Users end-points"],
    prefix = "/users"
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def create_posts():
    pass
