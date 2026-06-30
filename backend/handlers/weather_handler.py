from tools.weather import get_weather


def can_handle(message):
    """
    Detect weather-related queries.
    """

    text = message.lower()

    keywords = [
        "weather",
        "temperature",
        "forecast",
        "humidity",
        "wind"
    ]

    return any(word in text for word in keywords)


def handle(message):
    """
    Handle weather requests.
    """

    original = message.strip()
    lower = original.lower()

    prefixes = [
        "weather in",
        "temperature in",
        "forecast for",
        "forecast in",
        "weather",
        "temperature",
        "forecast",
        "humidity",
        "wind"
    ]

    city = original

    for prefix in prefixes:
        if lower.startswith(prefix):
            city = original[len(prefix):].strip()
            break

    if not city:
        return "Please specify a city.\nExample: Weather Hyderabad"

    weather = get_weather(city)

    if weather is None:
        return "City not found."

    if "error" in weather:
        return f"Weather Error: {weather['error']}"

    return (
        f"📍 {weather['city']}, {weather['country']}\n\n"
        f"🌡 Temperature : {weather['temperature']} °C\n"
        f"💧 Humidity    : {weather['humidity']}%\n"
        f"🌬 Wind Speed  : {weather['wind']} km/h"
    )