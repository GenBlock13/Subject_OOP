import tkinter as tk
from tkinter import *

import requests

root = tk.Tk(
    screenName="My App",
)

root.title("My App")
root.geometry('320x120')


def show_weather():
    city = entry_2.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    pressure = weather_data['main']['pressure']
    wind = weather_data['wind']['speed']
    return (f'Сейчас в  {city} {temperature}°C, {pressure} кПа')
    # print(f'Ощущается как {temperature_feels}°C, ветер {wind} м/с\n')


def window_position(w, h):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = w
    window_height = h
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


window_position(300, 200)

label1 = tk.Label(root, text="weather widget", anchor="n")
label1.pack()

frame_1 = tk.Frame(root)
frame_1.pack()

button_close = tk.Button(frame_1,
                         text="Close",
                         background="darkcyan",
                         command=root.destroy, anchor='sw'
                         )
button_close.grid(row=5, column=1)

label_2 = tk.Label(frame_1, text="Enter city name!", width=20)
label_2.grid(row=0, column=0)
entry_2 = tk.Entry(frame_1, background="lightblue")
entry_2.grid(row=0, column=1)

city = entry_2.get()


def change_text():
    city = entry_2.get()
    text = show_weather()
    forecast.delete(1.0, END)
    forecast.insert(1.0, text)


button_get = tk.Button(frame_1, text="Show weather", background="lightgreen", command=change_text)
button_get.grid(row=1, column=1)

forecast = tk.Text(frame_1, height=4, width=20, border="1")
forecast.grid(row=3, column=0, columnspan=3, sticky='sw', )

root.mainloop()
