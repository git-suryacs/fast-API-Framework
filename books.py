from typing import Dict

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'history'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title':'My fav Book!'}


@app.get("/books/{book_title}")
async def read_book(book_title: str) -> dict:
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
