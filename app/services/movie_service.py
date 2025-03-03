from sqlalchemy.orm import Session
from app.repositories.movie_repository import get_movie_by_id, create_movie, get_all_movies as repo_get_all_movies
from app.schemas.movie_schema import MovieSchema

def fetch_movie_by_id(db: Session, imdb_id: str):
    return get_movie_by_id(db, imdb_id)

def add_movie(db: Session, movie_data: MovieSchema):
    return create_movie(db, movie_data)


def get_all_movies(db: Session):
    return repo_get_all_movies(db)