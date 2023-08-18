from tkinter import *
import requests
import json
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("400x400") 
root.config(background='#A6E3E9')
root.resizable(0,0) 
root.title("Weather Forecast App")
 
 
# ----------------------Functions to fetch and display weather info
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    api_key = "8c003e98b7558912f3ac496916937137" 
    city_name=city_value.get()
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(url)
 
    # changing response from json to python readable 
    data = response.json()
 
 
    tfield.delete("1.0", "end")   
 
    if data['cod'] == 200:
        kelvin = 273 
        temp = int(data['main']['temp'] - kelvin)                                   
        feels_like_temp = int(data['main']['feels_like'] - kelvin)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed'] * 3.6
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timezone = data['timezone']
        cloudy = data['clouds']['all']
        description = data['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
          
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
    tfield.insert(INSERT, weather)   
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="#71C9CE", padx=5, pady=5 ).pack(pady= 20)
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()
