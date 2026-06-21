import requests
import time

def get_countries_by_region(region):
    url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            countries = response.json()
            return [country for country in countries if country.get('region', '').lower() == region.lower()]
        return []
    except Exception as e:
        print(f'Error fetching countries: {e}')
        return []

def get_current_weather(latitude, longitude):
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': True
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f'Error fetching weather: {e}')
        return None

countries = get_countries_by_region('europe')

results = []

WEATHER_CODES = {
    0: 'Clear sky',
    1: 'Mainly clear',
    2: 'Partly cloudy',
    3: 'Overcast',
    45: 'Fog',
    48: 'Depositing rime fog',
    51: 'Light drizzle',
    53: 'Moderate drizzle',
    55: 'Dense drizzle',
    61: 'Light rain',
    63: 'Moderate rain',
    65: 'Heavy rain',
    71: 'Light snow',
    73: 'Moderate snow',
    75: 'Heavy snow',
    80: 'Light rain showers',
    81: 'Moderate rain showers',
    82: 'Violent rain showers',
    95: 'Thunderstorm'
}

for country in countries[:5]:
    latitude = country['latlng'][0] if country.get('latlng') else None
    longitude = country['latlng'][1] if country.get('latlng') else None

    weather = get_current_weather(latitude, longitude) if latitude is not None and longitude is not None else None
    current_weather = weather.get('current_weather', {}) if weather else {}

    results.append({
        'name': country.get('name', {}).get('common', 'Name-N/A'),
        'capital': country['capital'][0] if country.get('capital') else 'Capital-N/A',
        'code': country.get('cca2', 'Code-N/A'),
        'latitude': latitude if latitude is not None else 'Latitude-N/A',
        'longitude': longitude if longitude is not None else 'Longitude-N/A',
        'temperature': current_weather.get('temperature', 'Temp-N/A'),
        'weather': WEATHER_CODES.get(current_weather.get('weathercode'),'Unknown weather')
    })

    time.sleep(0.5)

for r in results:
    print(f'{r["name"]:20} | {r["capital"]:20} | {r["code"]:10} | {r["temperature"]:10}°C | Current Weather: {r["weather"]}')
