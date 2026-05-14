def get_safety_status(wind_speed, weather_condition):

    if wind_speed > 12:
        return "Dangerous"

    elif weather_condition in ["Rain", "Thunderstorm"]:
        return "Dangerous"

    elif wind_speed > 6:
        return "Moderate"

    elif weather_condition in ["Mist", "Haze", "Fog"]:
        return "Moderate"

    else:
        return "Safe"