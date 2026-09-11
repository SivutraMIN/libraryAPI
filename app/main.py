from fastapi import FastAPI, HTTPException, status
from sqlmodel import SQLModel,create_engine,Field, Session, select
from pydantic import BaseModel


class Student(SQLModel, table=True):
    id: int  | None = Field(default=None, primary_key=True)
    name: str
    age: int
    year: int

class StudentResponse(BaseModel):
    name: str
    age: int
    year: int

class Admin(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    publisher: str
    publication_date: str
    isbn : str
    subject: str

sqlite_file_name = "db.db"
sqlite_url = f"sqlite:///app/database/{sqlite_file_name}"

engine = create_engine(sqlite_url,echo=True)
SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.get("/")
def root():
    return {"Message":"Welcome to our Library"}

#User
""" It has
+ Creating a User
+ Reading a User
+ Updating a User
+ Deleting a User
"""
# Creating User
@app.post("/createStudent", response_model=StudentResponse)
def create_user(student: Student):
    with Session(engine) as session:
        try:
            statement = Student(
                name=student.name,
                age=student.age,
                year=student.year,
            )
        except:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error with Requester Information")
        try:
            session.add(statement)
            session.commit()
        except:
            return HTTPException(status_code=status.WS_1011_INTERNAL_ERROR, detail="Error with Sending Information to Database")

        return StudentResponse(
            name=student.name,
            age=student.age,
            year=student.year
        )


@app.get("/user")
def get_all_user():
    with Session(engine) as session:
        statement = select(Student)
        users = session.exec(statement).all()
        return users

@app.put("/recreateUser")
def recreate_user():
    pass


@app.patch("/updateUser")
def updateUser():
    ...

@app.delete("/deleteUser")
def deleteUser():
    ...

#Books
"""It has
+ Creating a Book
+ Reading a Book
+ Updating a Book
+ Deleting a Book
"""

@app.get("/book/get-book")
def get_book():
    with Session(engine) as session:
        statement = select(Book)
        result = session.exec(statement).all()

        return result

@app.post("/book/post-book")
def post_book():
    pending_post = Book(
        
    )