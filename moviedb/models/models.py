from pydantic import BaseModel



class NewMovie(BaseModel):
    title: str
    overview: str
    release_date: str
    runtime: int
    rating: float
    actors: list
    genre: list
    country: str
    