from sqlalchemy import Column, Date, Integer, String
from app.database.db import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    imdb_id = Column(String(255), nullable=False, unique=True)
    poster = Column(String(255), nullable=False)
    release_date = Column(Date, nullable=False)
    title = Column(String(255), nullable=False)
    trailer_link = Column(String(255), nullable=False)