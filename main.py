from fastapi import FastAPI
from routes.user import router as user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}
