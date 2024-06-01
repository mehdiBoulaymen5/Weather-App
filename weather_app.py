import requests  
import json
import streamlit as st



def home_weather(city):
  api_key = "02aabeb108d4dcbd7e441f0b15c61e65"
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
  try:
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for any HTTP errors
  except requests.exceptions.HTTPError as err:
    print(f"Error: {err}")
  
  try:
    data = json.loads(response.text)
    if data['cod'] != 200:
      print(f"Error: {data['message']}")
  except json.JSONDecodeError as err:
      print(f"Error: failed to parse response JSON - {err}")


      #Extract relevant weather information
  weather_description = data['weather'][0]['description']
  temperature = data['main']['temp']
  humidity = data['main']['humidity']
  pressure = data['main']['pressure']

      #Convert temperature from Kelvin to Celcius
  temperature = round(temperature - 273.15, 2)

      #Print the weather forecast
  st.write(data)
  st.write(f"Weather in {city}: {weather_description} ")
  st.write(f"Temperature: {temperature}'C")
  st.write(f"humidity: {humidity}")
  st.write(f"Pressure: {pressure}")
st.header("Check the current weather")
with st.container():
  image_column_1, image_column_2 = st.columns(2)
  with image_column_1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlQGK1IYsWsEIqGxdammw22AmFq0oDADJzZA&s")
  with image_column_2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTCyDP_U9g-oDPVqdY59F01k13oA_ZbT5Lkw&s")
             
  
city = st.text_input("Enter city name")
if st.button("Get weather"):
  home_weather(city)

