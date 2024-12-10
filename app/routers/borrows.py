
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db


#Router for books
@router.post("/create-book", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/books", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@router.get("/books/{id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
  
@router.put("/book/update/{id}", response_model=schemas.Book)
def update_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/book/delete/{id}")
def delete(id:int, db:Session=Depends(get_db)):
    book = crud.delete_book(db, book_id=id)
    if not book:
        return raise HTTPException(status_code=404, detail="Book not found")
    return book
