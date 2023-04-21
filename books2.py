from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    id: Optional[int] = Field(title='Id is optional field')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=99)
    rating: int = Field(gt=-1, lt=6)

    class Config:
        schema_extra = {
            'example':{
                'title': 'A new book',
                'author': 'surya',
                'description': 'A new description of a book',
                'rating' : 5
            }
        }


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


@app.get("/books/{book_id}")
async def read_book_by_id(book_id:int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/")
async def read_books_by_rating(book_rating :int):
    list_of_books = []
    for book in BOOKS:
        if book.rating == book_rating :
            list_of_books.append(book)
    return list_of_books


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update_book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
