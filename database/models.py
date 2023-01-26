from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):

    __tablename__ = "author"

    author_id = Column(Integer, primary_key=True)

    name = Column(String)

    quotes = relationship("Quote", backref=backref("author"))


class Quote(Base):

    __tablename__ = "quote"

    quote_id = Column(Integer, primary_key=True)

    author_id = Column(Integer, ForeignKey("author.author_id"))

    text = Column(String)