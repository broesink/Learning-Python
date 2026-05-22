import requests
import json

def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "results" in data:
            result = data["results"][0]
            return result["latitude"], result["longitude"]
        return None, None
    else:
        print(f"Oops, something went wrong with the coordinates: {response.status_code}")

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        return weather["temperature"]
    else:
        print(f"Oops, something went wrong with retreiving weather info: {response.status_code}")

city = input("Where do you live? ")
lat, lon = get_coordinates(city)
temperature = get_weather(lat, lon)
print(f"The temperature in {city} is {temperature} degrees.")

