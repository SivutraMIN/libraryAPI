from fastapi import FastAPI
from router.books import router as books
from router.admin import router as admin

app = FastAPI()

app.include_router(books)
app.include_router(admin)
