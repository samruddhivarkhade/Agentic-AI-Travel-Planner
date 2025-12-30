import requests
from typing import Dict, List

# City to coordinates mapping (can be expanded)
CITY_COORDINATES = {
    "goa": {"lat": 15.2993, "lon": 74.1240},
    "delhi": {"lat": 28.6139, "lon": 77.2090},
    "mumbai": {"lat": 19.0760, "lon": 72.8777},
    "bangalore": {"lat": 12.9716, "lon": 77.5946},
    "chennai": {"lat": 13.0827, "lon": 80.2707},
    "hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "kolkata": {"lat": 22.5726, "lon": 88.3639},
    "jaipur": {"lat": 26.9124, "lon": 75.7873}
}

def get_weather(city: str, days: int = 3) -> List[Dict]:
    """
    Get weather forecast for a city using Open-Meteo API
    """
    city_key = city.lower()

    if city_key not in CITY_COORDINATES:
        return [{"error": "City not supported"}]

    lat = CITY_COORDINATES[city_key]["lat"]
    lon = CITY_COORDINATES[city_key]["lon"]

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return [{"error": "Weather API failed"}]

    data = response.json()

    forecast = []
    for date, temp in zip(
        data["daily"]["time"][:days],
        data["daily"]["temperature_2m_max"][:days]
    ):
        forecast.append({
            "date": date,
            "max_temperature_celsius": temp
        })

    return forecast

# Testing the tool directly
if __name__ == "__main__":
    weather = get_weather("Goa", days=3)
    print("Weather Forecast:")
    for day in weather:
        print(day)
