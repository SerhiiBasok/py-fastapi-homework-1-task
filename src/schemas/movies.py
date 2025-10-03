from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import date

class MovieDetailResponseSchema(BaseModel):
    id: int
    name: str
    date: date
    score: float
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: float
    revenue: float
    country: str

    model_config = ConfigDict(from_attributes=True)

class MovieListResponseSchema(BaseModel):
    movies: list[MovieDetailResponseSchema]
    prev_page: Optional[int]
    next_page: Optional[int]
    total_pages: int
    total_items: int

    model_config = ConfigDict(from_attributes=True)



