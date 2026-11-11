import httpx

URL = "https://api.open-meteo.com/v1/forecast"

response = httpx.get(
    URL,
    params={"latitude": 24.86, "longitude": 67.01, "current": "temperature_2m"},
    timeout=10,
)

print(response.status_code)
data = response.json()
print(data["current"]["temperature_2m"])
