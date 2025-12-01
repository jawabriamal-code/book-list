from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# רשימת ספרים בזיכרון
books = []

# מודל של ספר
class Book(BaseModel):
    id: int
    title: str
    author: str

# GET - כל הספרים
@app.get("/books")
def get_books():
    return books

# GET - ספר לפי מזהה
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

# POST - הוספת ספר
@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added", "book": book}

# DELETE - מחיקת ספר לפי מזהה
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}
