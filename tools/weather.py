import requests


def get_weather(city):
    """
    Returns current weather for a city using Open-Meteo.
    No API key required.
    """

    try:
        # Get coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo = requests.get(
            geo_url,
            params={
                "name": city,
                "count": 1
            },
            timeout=10
        ).json()

        if "results" not in geo:
            return None

        place = geo["results"][0]

        latitude = place["latitude"]
        longitude = place["longitude"]
        city_name = place["name"]
        country = place["country"]

        # Current weather
        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
            },
            timeout=10
        ).json()

        current = weather["current"]

        return {
            "city": city_name,
            "country": country,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
            "code": current["weather_code"]
        }

    except Exception as e:
        return {"error": str(e)}