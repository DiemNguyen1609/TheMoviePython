from fastapi import FastAPI
from route.user_route import router as user_router

app = FastAPI()

app.include_router(user_router, tags=["Users"], prefix="/Users")

@app.get("/")
def root():
    return {"message": "Hello World"}

