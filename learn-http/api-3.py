# 3. Two APIs in a row. Open-Meteo has a second API that finds a city's coordinates by name. 
# Try this in your browser first:

# Copy
# https://geocoding-api.open-meteo.com/v1/search?name=Multan&count=1
# Write find_city(name), which returns a city's latitude and longitude using a Pydantic model for the
#  response.'
# ' Then write weather_for(name), which calls find_city() and then get_forecast(). '
# 'What does the geocoding API send back for a city that doesn't exist, such as Notacity? 
# Make find_city() raise a ValueError with a clear message when that happens.

import httpx
from pydantic import BaseModel

URL = "https://api.open-meteo.com/v1/forecast"
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"


class CityCheck(BaseModel):
    name: str
    longitude: float
    latitude: float


def find_city(name: str) -> CityCheck:
    response = httpx.get(
        GEO_URL,
        params={"name": name, "count": 1},
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        raise ValueError(f"City '{name}' not found")

    city = data["results"][0]

    return CityCheck.model_validate(city)


def weather_for(name: str):
    city = find_city(name)

    response = httpx.get(
        URL,
        params={
            "latitude": city.latitude,
            "longitude": city.longitude,
            "current": "temperature_2m"
        },
        timeout=10,
    )

    response.raise_for_status()

    return (f"temperature: {response.json()["current"]["temperature_2m"]}")

try:
    print(weather_for("Multan"))
    print(find_city("Notacity"))
except ValueError as error:
        print(f"{error}")