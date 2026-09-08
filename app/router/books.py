from fastapi import APIRouter

router = APIRouter(prefix="books")

@router.get("/")
def root():
    return {"Message":"Welcome to our Library"}