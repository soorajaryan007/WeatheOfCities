#!/usr/bin/env python
# coding: utf-8

# Weatherstack.com

# In[10]:


import requests

# Define the API key and base URL
API_KEY = 'bf1cb2e920896d89bfb261f0cd282681'
BASE_URL = 'http://api.weatherstack.com/current'

# Define the location you want to get weather information for
location = 'Manali'

# Construct the full API URL with the query parameter and API key
url = f"{BASE_URL}?access_key={API_KEY}&query={location}"

# Send a GET request to the WeatherStack API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract and display the weather details
    if 'current' in data:
        current_weather = data['current']
        print(f"Weather in {location}:")
        print(f"Temperature: {current_weather['temperature']}°C")
        print(f"Weather Description: {current_weather['weather_descriptions'][0]}")
        print(f"Humidity: {current_weather['humidity']}%")
        print(f"Wind Speed: {current_weather['wind_speed']} km/h")
    else:
        print(f"Error: Could not retrieve weather data for {location}")
else:
    print(f"Error: {response.status_code}, {response.text}")


# In[ ]:




