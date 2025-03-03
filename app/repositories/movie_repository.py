from sqlalchemy.orm import Session
from app.models.movie import Movie

def get_movie_by_id(db: Session, imdb_id: str):
    return db.query(Movie).filter(Movie.imdb_id == imdb_id).first()

def create_movie(db: Session, movie_data):
    movie = Movie(**movie_data.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def get_all_movies(db: Session):
    return db.query(Movie).all()