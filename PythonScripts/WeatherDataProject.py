from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import requests
import json

root = Tk()
root.title("Weather Forecast")
root.geometry("400x250")

# Function to get forecast data for a given city
def get_forecast(city):
    try:
        api_key = "3d79ae791eeda9da806485efcebfae70"
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=3d79ae791eeda9da806485efcebfae70&units=metric"
        api_request = requests.get(url)
        api = json.loads(api_request.content)
        forecast = api["list"]
        return forecast
    except Exception as e:
        return None

# Function to display forecast data for a given city
def display_forecast():
    city = cityEntry.get()
    forecast = get_forecast(city)

    if forecast is None:
        messagebox.showerror("Error", "Could not get forecast data. Please try again.")
        return

    # Clear previous forecast data if any
    for widget in frame.winfo_children():
        widget.destroy()

    # Display forecast data in a table
    for i in range(len(forecast)):
        # Get the date and time of the forecast data
        date_time = forecast[i]["dt_txt"]
        date = date_time.split()[0]
        time = date_time.split()[1][:5]

        # Get the temperature, humidity and weather description of the forecast data
        temp = forecast[i]["main"]["temp"]
        humidity = forecast[i]["main"]["humidity"]
        weather_desc = forecast[i]["weather"][0]["description"]

        # Create labels for the forecast data and add them to the table
        dateLabel = Label(frame, text=date, font=("Helvetica", 10))
        dateLabel.grid(row=i, column=0, padx=10, pady=5)
        timeLabel = Label(frame, text=time, font=("Helvetica", 10))
        timeLabel.grid(row=i, column=1, padx=10, pady=5)
        tempLabel = Label(frame, text=f"{temp:.1f} °C", font=("Helvetica", 10))
        tempLabel.grid(row=i, column=2, padx=10, pady=5)
        humidityLabel = Label(frame, text=f"{humidity}%", font=("Helvetica", 10))
        humidityLabel.grid(row=i, column=3, padx=10, pady=5)
        weatherLabel = Label(frame, text=weather_desc.title(), font=("Helvetica", 10))
        weatherLabel.grid(row=i, column=4, padx=10, pady=5)

# Create the GUI elements
titleLabel = Label(root, text="Enter a city name to get the weather forecast", font=("Helvetica", 12))
titleLabel.pack(pady=10)

cityEntry = Entry(root, width=30, font=("Helvetica", 10))
cityEntry.pack()

getForecastButton = Button(root, text="Get Forecast", command=display_forecast)
getForecastButton.pack(pady=10)

# Create a frame to display the forecast data
frame = LabelFrame(root, text="Forecast Data", padx=10, pady=10)
frame.pack(fill="both", expand="yes", padx=10, pady=10)

root.mainloop()
