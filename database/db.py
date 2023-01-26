import os
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from database.models import Author, Quote, Base

dirname = os.path.dirname(__file__)
sqlite_filepath = os.path.join(dirname, '..', 'data', 'database.db')
engine = create_engine(f"sqlite:////{sqlite_filepath}")

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def add_quote(text, author_name):
    quote = (
        session.query(Quote)
        .join(Author)
        .filter(Quote.text == text)
        .filter(
            and_(
                Author.name == author_name
            )
        )
        .one_or_none()
    )

    if quote is not None:
        return

    author = (
        session.query(Author)
        .filter(Author.name == author_name)
        .one_or_none()
    )

    if author is None:
        author = Author(name=author_name)
        session.add(author)

    quote = Quote(text=text, author=author)
    session.add(quote)

    session.commit()
