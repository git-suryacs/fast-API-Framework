from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title :str
    author :str
    description :str
    rating :int



BOOKS = [
    Book(1, 'Computer Science Pro', 'surya', 'A very nice book', 5),
    Book(2, 'Be fast with FastAPI', 'surya', 'This is a great book', 5),
    Book(3, 'Master Endpoints', 'surya', 'An awesome book', 5),
    Book(4, 'HP1', 'author1', 'Book desc', 2),
    Book(5, 'HP2', 'author2', 'Book desc', 3),
    Book(6, 'HP3', 'author3', 'Book desc', 1)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)