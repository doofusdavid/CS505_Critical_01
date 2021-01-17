# Python Script to retrieve current temperature and display it.

# Hide API key from github
# Key found here: https://home.openweathermap.org/api_keys

import config

url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
