from typing import Optional, List
from sqlalchemy import and_
from sqlalchemy.orm import Session
from ..db_model.book import BookTable
from ..model.book import SearchCondBook


def find_all(db_session: Session) -> List[BookTable]:
    """
    Find books.
    :param db_session: SQLAlchemy DBSession
    :return: search result
    """
    return db_session.query(BookTable).all()


def find_by_id(db_session: Session, *, book_id: int) -> Optional[BookTable]:
    """
    Find a book by book id.
    :param db_session: SQLAlchemy DBSession
    :param book_id: book id
    :return: search result
    """
    return db_session.query(BookTable).filter(BookTable.id == book_id).first()


def find(db_session: Session, *, search_cond: SearchCondBook) -> List[BookTable]:
    """
    Find books by search condition.
    :param db_session: SQLAlchemy DBSession
    :param search_cond: search condition
    :return: search result
    """
    filters = list()
    if search_cond.isbn:
        filters.append(and_(BookTable.isbn == search_cond.isbn))
    if search_cond.title:
        filters.append(and_(BookTable.title.like(search_cond.title)))
    if search_cond.author:
        filters.append(and_(BookTable.author.like(search_cond.author)))
    if search_cond.publisher:
        filters.append(and_(BookTable.publisher.like(search_cond.publisher)))
    if search_cond.publish_date_from:
        filters.append(and_(BookTable.publish_date >= search_cond.publish_date_from))
    if search_cond.publish_date_to:
        filters.append(and_(BookTable.publish_date <= search_cond.publish_date_to))
    return db_session.query(BookTable).filter(filters).all()
