from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.services.movie_service import fetch_movie_by_id, add_movie,get_all_movies
from app.schemas.movie_schema import MovieSchema

router = APIRouter(prefix="/movies", tags=["movies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/movie/{imdb_id}")
def get_movie(imdb_id: str, db: Session = Depends(get_db)):
    return fetch_movie_by_id(db, imdb_id)

@router.post("/")
def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):
    return add_movie(db, movie)

@router.get("/all")
def create_movie(db: Session = Depends(get_db)):
    return get_all_movies(db)