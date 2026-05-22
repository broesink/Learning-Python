import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 38.54,
    "longitude": -0.13,
    "current_weather": True,
    "timezone": "Europe/Madrid"
}

response = requests.get(url, params=params)

print(f"Status code: {response.status_code}") #Always check the status, else the script may crash without knowing what happened exactly

data = response.json()

weather = data["current_weather"]
print(f"Temperature: {weather['temperature']}°C")
print(f"Wind speed: {weather['windspeed']} km/h")
current_time = weather["time"].split("T")[1]
print(f"Current time: {current_time}")

import json

print(json.dumps(data,indent=4))