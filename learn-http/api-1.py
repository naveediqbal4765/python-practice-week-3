# 1. Several cities. Use get_forecast() to print the temperature for each of these cities, 
# one per line, as Karachi: 31.2°C:

# Copy
import httpx

CITIES = {
    "Karachi": (24.86, 67.01),
    "Lahore": (31.55, 74.34),
    "Islamabad": (33.69, 73.06),
    "Quetta": (30.18, 66.98),
}

def get_forecast(lat, long):
    URL = "https://api.open-meteo.com/v1/forecast"

    response = httpx.get(
        URL, 
        params={"latitude": lat, "longitude": long, "current": "temperature_2m"}, 
        timeout=10,
)
    return response.json()["current"]["temperature_2m"]

for key, value in CITIES.items():
    print(f"{key}: {get_forecast(value[0],value[1])}")

    



