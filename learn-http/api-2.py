# 2. Fail clearly. Add a fifth city with a latitude of 95. 
# Change your loop so that one bad city prints a clear message naming the city and 
# the API's reason, and the other cities still print.
import httpx

CITIES = {
    "Karachi": (24.86, 67.01),
    "Lahore": (31.55, 74.34),
    "Islamabad": (33.69, 73.06),
    "Quetta": (30.18, 66.98),
    "Gilgit": (95, 89.9) 
}

def get_forecast(lat, long):
    URL = "https://api.open-meteo.com/v1/forecast"

    response = httpx.get(
        URL, 
        params={"latitude": lat, "longitude": long, "current": "temperature_2m"}, 
        timeout=10,
    )
    response.raise_for_status() 
    
    return response.json()["current"]["temperature_2m"]

for key, value in CITIES.items():
    try:
        print(f"{key}: {get_forecast(value[0], value[1])}")
    except httpx.HTTPStatusError as error:
        print(f"{key}: {error.response.text}")

