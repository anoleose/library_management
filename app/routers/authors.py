from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()
#Router for authors
@router.post("/create-author", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)

@router.get("/authors", response_model=list[schemas.Author])
def get_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)

@router.get("/author/{id}", response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.put("/author/update/{id}", response_model=schemas.Author)
def update_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.update_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

  
@router.delete("/author/delete/{id}", response_model=schemas.Author)
def delete_author(author_id:int, db:Session=Depends(get_db)):
    author = crud.delete_author(db, author_id=id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found") 
    return author




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
