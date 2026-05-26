from fastapi import APIRouter
import json
import os

from app.services.weather_service import fetch_weather
from app.services.safety_service import get_safety_status

router = APIRouter()

# Load beaches from JSON file
def load_beaches():
    json_path = os.path.join(os.path.dirname(__file__), "../../beaches.json")
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)

@router.get("/beaches")
def get_beaches():
    beaches = load_beaches()
    updated_beaches = []

    for beach in beaches:
        lat = beach["lat"]
        lon = beach["lon"]

        weather = fetch_weather(lat, lon)

        if not weather:
            updated_beach = {
                **beach,
                "temperature": "N/A",
                "weather": "N/A",
                "wind_speed": "N/A",
                "safety_status": "Unavailable"
            }
            updated_beaches.append(updated_beach)
            continue

        safety_status = get_safety_status(
            weather["wind_speed"],
            weather["weather"]
        )

        updated_beach = {
            **beach,
            "temperature": weather["temperature"],
            "weather": weather["description"],
            "wind_speed": weather["wind_speed"],
            "safety_status": safety_status,
        }

        updated_beaches.append(updated_beach)

    return updated_beaches


@router.get("/beaches/{beach_id}")
def get_beach(beach_id: int):

    if beach_id < 0 or beach_id >= len(beaches):
        return {"error": "Beach not found"}

    return beaches[beach_id]


@router.get("/search")
def search_beach(name: str):

    filtered = []

    for beach in beaches:

        if name.lower() in beach["name"].lower():
            filtered.append(beach)

    return filtered