from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# New
book_db = [
    {
        "title":"The C Programming",
        "price": 720
    },
    {
        "title":"Learn Python the Hard Way",
        "price": 870
    },
    {
        "title":"JavaScript: The Definitive Guide",
        "price": 1369
    },
    {
        "title":"Python for Data Analysis",
        "price": 1394
    },
    {
        "title":"Clean Code",
        "price": 1500
    },
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/book/")
async def get_books():
    return book_db

@app.get("/book/{book_id}")
async def get_book(book_id: int):
    return book_db[book_id-1]

class Book(BaseModel):
    title: str
    price: float
    
#create new book
@app.post("/book")
async def create_book(book: Book):
    book_db.append(book.dict())
    return book_db[-1]
