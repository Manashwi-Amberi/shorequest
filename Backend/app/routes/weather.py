from fastapi import APIRouter, HTTPException
from app.services.weather_service import fetch_weather

router = APIRouter()

@router.get("/{city}")
def get_weather(city: str):

    weather = fetch_weather(city)

    if not weather:
        raise HTTPException(
            status_code=404,
            detail=f"City '{city}' not found"
        )

    return {
        "city": city,
        **weather
    }