from sqlalchemy import Column, Integer, String
from app.database import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    author = Column(String(255), index=True, unique=False)
    title = Column(String(255), index=True, unique=True)

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __repr__(self):
        return '<Book %r>' % (self.author + self.title)
