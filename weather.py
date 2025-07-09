import datetime as dt
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "ac4e49e5b74ca479803c8c98e5f80166"
CITY = ("London")

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = (kelvin - 32) * 5/9
    fahrenheit = (celsius * 9) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

print(f"Temperature in {CITY} {temp_celsius:.2f}<UNK>C or {temp_fahrenheit}<UNK>F")
