
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db


#Router for books
@router.post("/create-borrow", response_model=schemas.Borrow)
def create_borrow(borrow: schemas.BorrowCreate, db: Session = Depends(get_db)):
    return crud.create_borrow(db, borrow)

@router.get("/borrows", response_model=list[schemas.Borrow])
def get_borrows(db: Session = Depends(get_db)):
    return crud.get_borrows(db)

@router.get("/borrow/{id}", response_model=schemas.Borrow)
def get_borrow(borrow_id: int, db: Session = Depends(get_db)):
    borrow = crud.get_borrow(db, borrow_id)
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return borrow
  
@router.put("/borrow/update/{id}", response_model=schemas.Borrow)
def update_borrow(borrow_id: int, db: Session = Depends(get_db)):
    borrow = crud.update_borrow(db, borrow_id)
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return borrow

@router.delete("/borrow/delete/{id}")
def delete_borrow(id:int, db:Session=Depends(get_db)):
    borrow = crud.delete_borrow(db, borrow_id=id)
    if not borrow:
        return raise HTTPException(status_code=404, detail="Borrow not found")
    return borrow
