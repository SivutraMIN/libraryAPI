from fastapi import APIRouter
from sqlmodel import Session,select
from database.database import engine
import database.models as model

router = APIRouter(prefix="books")

@router.get("/")
def root():
    return {"Message":"Welcome to our Library"}


@router.get("/user")
def get_all_user():
    with Session(engine) as session:
        statement = select(model.Student)

        users = session.exec(statement).all()

        return users

