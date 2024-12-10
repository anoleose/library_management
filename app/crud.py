from sqlalchemy.orm import Session
from app.models import Author, Book, Borrow
from app.schemas import AuthorCreate, BookCreate, BorrowCreate, AuthorUpdate, BookUpdate, BorrowUpdate

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
    author = get_author_by_id(db=db, author_id=author_id)
    if author
    	author.first_name = AuthorUpdate.first_name
    	author.surname = AuthorUpdate.surname
    	author.date_of_birth = AuthorUpdate.date_of_birth
    	db.commit()
    	db.refresh(author)
    	return author
	

def delete_author(db: Session, author_id: int):
    author = get_author_by_id(db, author_id)
    if author:
        db.delete(author)
        db.commit()


# CRUD for books
def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db:Session, book_id: int):
    book = get_book_by_id(db=db, book_id=book_id)
    if book:
    	book.title = BookUpdate.title
    	book.description = BookUpdate.description
    	book.author_id = BookUpdate.author_id
	book.copies_available = BookUpdate.copies_available 
    	db.commit()
    	db.refresh(book)
    	return book
	

def delete_book(db: Session, book_id: int):
    book = get_author_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()





