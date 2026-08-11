# Finding the Weather condition of a place:

import requests

base_url = "https://geocoding-api.open-meteo.com/v1/search"

def get_city_info(name):
    url = f"{base_url}?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        city_data = response.json()
        return city_data['results'][0]

    else:
        print(f"Failed to get data: error code: {response.status_code}")


city = input("Enter city name: ").capitalize()
city_info = get_city_info(city)

if city_info:
    print(f"Country : {city_info['country']}")
    print(f"Latitude : {city_info['latitude']}")
    print(f"Longitude : {city_info['longitude']}")

print()
print()

weather_url = "https://api.open-meteo.com/v1/forecast"

def weather_info(latitude, longitude):
    url = f"{weather_url}?latitude={latitude}&longitude={longitude}&current=temperature_2m,apparent_temperature,relative_humidity_2m,precipitation,wind_speed_10m,weather_code"
    responses = requests.get(url)

    if responses.status_code == 200:
        weather_data = responses.json()
        return weather_data['current']['temperature_2m']

    else:
        print(f"Failed to retrieve the data (error code): {responses.status_code}")


temperature = weather_info(city_info['latitude'], city_info['longitude'])

if temperature:
    print(f"Temperature: {temperature} °C")