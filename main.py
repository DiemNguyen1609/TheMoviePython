import logging
logging.basicConfig(level=logging.DEBUG,format='\n%(asctime)s - %(levelname)s \n %(message)s \n')

from fastapi import FastAPI
from route.user_route import router as user_router
from route.movie_route import router as movie_router

app = FastAPI()

app.include_router(user_router, tags=["Users"], prefix="/Users")
app.include_router(movie_router, tags=["Movies"], prefix="/Movies")

@app.get("/")
def root():
    return {"message": "Hello World"}

