from fastapi import FastAPI
from app.api.movies import router as movie_router
from app.database.db import engine, Base

from .models.movie import Movie

app = FastAPI()

# Include the movie API routes
app.include_router(movie_router)

# Create all tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the Movies API"}
