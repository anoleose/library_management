from sqlalchemy.orm import Session
from app.models import Author, Book, Borrow
from app.schemas import AuthorCreate, BookCreate, BorrowCreate

# CRUD for Authors
def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    return db.query(Author).all()

def get_author_by_id(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def update_author(db:Session, author_id: int):
	get_author = get_author_by_id(db=db, author_id=author_id)
	get_author.title = author.first_name
	get_author.surname = author.surname
   	 get_author.date_of_birth = author.date_of_birth
	db.commit()
	db.refresh(get_author)
	return get_author
	

def delete_author(db: Session, author_id: int):
    author = get_author_by_id(db, author_id)
    if author:
        db.delete(author)
        db.commit()

# Similarly, add CRUD for books and borrows...

