from fastapi import APIRouter, HTTPException
from controller.movie_controller import MovieController

router = APIRouter()

@router.get("/movie/")
async def get_all_movies():
    return MovieController.get_movies()

@router.get("/movie/{movie_id}")
async def get_movie_detail(movie_id: str):
    movie = MovieController.get_movie(movie_id)
    if movie:
        return movie
    raise HTTPException(status_code=404, detail="Movie not found")
