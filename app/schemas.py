from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class AuthorBase(BaseModel):
    first_name: str
    surname: str
    date_of_birth: date

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    copies_available: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True


class BorrowBase(BaseModel):
    book_id: int
    reader_name: str
    date_of_issue: datetime
    return_date: Optional[datetime]

class BorrowCreate(BorrowBase):
    pass

class Borrow(BorrowBase):
    id: int
    class Config:
        orm_mode = True




class AuthorUpdate(BaseModel):
    first_name: Optional[str] = None
    surname: Optional[str] = None
    date_of_birth: Optional[datetime] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author_id: Optional[int] = None  # ForeignKey to Author
    copies_available: Optional[int] = None

class BorrowUpdate(BaseModel):
    book_id: Optional[int] = None  # ForeignKey to Author
    reader_name: Optional[str] = None
    date_of_issue: Optional[datetime] = None
    return_date: Optional[datetime] = None  # Datetime field to update











