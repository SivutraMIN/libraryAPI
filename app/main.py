from fastapi import FastAPI
from sqlmodel import SQLModel,create_engine,Field, Session, select

class Student(SQLModel, table=True):
    id: int  | None = Field(default=None, primary_key=True)
    name: str
    age: int



sqlite_file_name = "db.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url,echo=True)
SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.get("/")
def root():
    return {"Message":"Welcome to our Library"}

@app.post("/createStudent")
def create_user():
    with Session(engine) as session:
        statement = Student(name="John", age="20")
        session.add(statement)
        session.commit()

@app.get("/user")
def get_all_user():
    with Session(engine) as session:
        statement = select(Student)
        
        users = session.exec(statement).all()

        return users

