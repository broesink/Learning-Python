import requests
import json
import os
from datetime import datetime

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
        print(f"Oops, something went wrong with retrieving weather info: {response.status_code}")

def save_to_history(city, temperature):
    history = []
    
    if os.path.exists("history.json"):
        with open("history.json", "r") as file:
            history = json.load(file)

    new_search = {
        "city" : city,
        "temperature": temperature,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    history.append(new_search)

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

def show_history():

    history = []

    if os.path.exists("history.json"):
        with open("history.json", "r") as file:
            history = json.load(file)

    for items in history[-3:]:
        print(f"City: {items['city']} | Temperature: {items['temperature']} | Time: {items['time']}")
        

show_history()
city = input("Where do you live? ")
lat, lon = get_coordinates(city)

if lat is None:
    print("City not found, try again.")
else:
    temperature = get_weather(lat, lon)
    print(f"The temperature in {city} is {temperature} degrees.")
    save_to_history(city, temperature)