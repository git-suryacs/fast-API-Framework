from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='Id is optional field')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=99)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2023)

    class Config:
        schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'surya',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2019
            }
        }


BOOKS = [
    Book(1, 'Computer Science Pro', 'surya', 'A very nice book', 5, 1999),
    Book(2, 'Be fast with FastAPI', 'surya', 'This is a great book', 5, 2005),
    Book(3, 'Master Endpoints', 'surya', 'An awesome book', 5, 2009),
    Book(4, 'HP1', 'author1', 'Book desc', 2, 2007),
    Book(5, 'HP2', 'author2', 'Book desc', 3, 2010),
    Book(6, 'HP3', 'author3', 'Book desc', 1, 2022)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
    list_of_books = []
    for book in BOOKS:
        if book.rating == book_rating:
            list_of_books.append(book)
    return list_of_books


@app.get("/books/publish/{year}", status_code=status.HTTP_200_OK)
async def read_books_by_published_year(year: int = Path(gt=1999)):
    list_of_books = []
    for book in BOOKS:
        if book.published_date == year:
            list_of_books.append(book)
    return list_of_books


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(book_id: int = Path(gt=0)):
    book_changed = False
    for book in BOOKS:
        if book.id == book_id:
            BOOKS.remove(book)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
