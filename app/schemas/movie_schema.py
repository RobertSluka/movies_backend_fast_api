from pydantic import BaseModel
from datetime import date

class MovieSchema(BaseModel):
    imdb_id: str
    title: str
    release_date: date
    poster: str
    trailer_link: str

    class Config:
        orm_mode = True
