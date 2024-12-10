from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    surname = Column(String, index=True)
    date_of_birth = Column(Date)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    copies_available = Column(Integer)

    author = relationship("Author", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")


class Borrow(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    reader_name = Column(String)
    date_of_issue = Column(DateTime)
    return_date = Column(DateTime, nullable=True)

    book = relationship("Book", back_populates="borrows")

