from fastapi import APIRouter

from app.data.beaches_data import beaches
from app.services.weather_service import fetch_weather
from app.services.safety_service import get_safety_status

router = APIRouter()

@router.get("/beaches")
def get_beaches():

    updated_beaches = []

    for beach in beaches:

        lat = beach["lat"]
        lon = beach["lon"]

        weather = fetch_weather(lat, lon)

        if not weather:
            updated_beaches.append({
                "name": beach["name"],
                "city": beach["city"],
                "temperature": "N/A",
                "weather": "N/A",
                "wind_speed": "N/A",
                "safety_status": "Unavailable"
            })
            continue

        safety_status = get_safety_status(
            weather["wind_speed"],
            weather["weather"]
        )

        updated_beach = {
            "name": beach["name"],
            "city": beach["city"],
            "temperature": weather["temperature"],
            "weather": weather["description"],
            "wind_speed": weather["wind_speed"],
            "safety_status": safety_status,
            "img": beach["img"],
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