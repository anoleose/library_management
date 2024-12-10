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



