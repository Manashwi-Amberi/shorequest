from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.routes import beaches, weather


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the Frontend images folder
images_path = os.path.join(os.path.dirname(__file__), "../../Frontend/images")
app.mount("/images", StaticFiles(directory=images_path), name="images")


@app.get("/")
def home():
    return {"message": "Welcome to the ShoreQuest API!"}


app.include_router(beaches.router)
app.include_router(weather.router, prefix="/weather")