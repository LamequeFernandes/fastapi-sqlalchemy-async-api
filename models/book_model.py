from sqlalchemy import Column, Integer, String, DateTime

from database.config import settings

import datetime


class BookModel(settings.Base):
    __tablename__ = 'book'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100), nullable=False)
