# Python Script to retrieve current temperature and display it.

# Hide API key from github
# Key found here: https://home.openweathermap.org/api_keys


import config
import requests, urllib.parse, json


def KelvinToFahrenheit(k_temp):
    return round((k_temp * (9 / 5) - 459.67), 2)


url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

formatted_url = url.format(city=urllib.parse.quote_plus(config.city), api_key=config.api_key)
response = requests.get(formatted_url)
result = json.loads(response.content)

print("City: {}".format(config.city))
print("Current Weather: {}".format(result['weather'][0]['description']))
print("Current Temperature: {} °F".format(KelvinToFahrenheit(result['main']['temp'])))
