import requests

API_KEY = "f76e5c5fa05a6ff7ae7e67c78e48ef16"

def fetch_weather(lat, lon):

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }