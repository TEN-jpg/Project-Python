import requests
import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


root = tk.Tk()
root.title("Weather App")
root.geometry("900x1000")
root.config(bg = "#aee6ff")

tite_lable = tk.Label(root, text="Weather App", font=('Arial', 20, 'bold'), bg= "#d9faff")
tite_lable.pack(pady=10)

city_entry = tk.Entry(root, font=('Arial', 20), bg="#ffffff", fg="#333333", width= 25)
city_entry.pack(pady=5)
city_entry.insert(0, "Enter a City name...")

def rm_placeholder(event):  #n Tkinter, when you bind a function to a widget event (like a mouse click or focus),Tkinter automatically sends an “event object” to that function.
    if city_entry.get() == "Enter a City name...":
        city_entry.delete(0, tk.END)

city_entry.bind("<FocusIn>", rm_placeholder)


def fetch_weather():
    city = city_entry.get()
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    data = response.json()
    if data.get('cod') == '404' or data.get('cod') == 404:
        result_city.config(text="City not found Please enter a valid city name...")
        result_weather.config(text="")
        result_temp.config(text="")
        result_humidity.config(text="")
        result_coord.config(text="")
    else:
        result_city.config(text=f"City: {data['name']}")
        result_weather.config(text=f"Weather: {data['weather'][0]['description']}") #weather is a list; [0] picks the first condition.
        result_temp.config(text=f"Temprature: {data['main']['temp']}°C")
        result_humidity.config(text=f"Humidity: {data['main']['humidity']}%")
        result_coord.config(text=f"Co-ordianates: {data['coord']}")


def your_location():
    result_city.config(text="Just look outside, bruh!")
    result_weather.config(text="")
    result_temp.config(text="")
    result_humidity.config(text="")
    result_coord.config(text="")


get_button = tk.Button(root, text="Get Weather", font=("Arial", 12,"bold"), bg="#00aaff", fg="white")
get_button.pack(pady=10)
get_button.config(command=fetch_weather)

current_button = tk.Button(root, text="Your Location 📍", font=("Arial", 12, "bold"), bg="#00cc88", fg="white", command=your_location)
current_button.pack(pady=5)

result_city = tk.Label(root, text="", font=("Arial", 14), bg="#aee6ff")
result_city.pack(pady=2)

result_weather = tk.Label(root, text="", font=("Arial", 14), bg="#aee6ff")
result_weather.pack(pady=2)

result_temp = tk.Label(root, text="", font=("Arial", 14), bg="#aee6ff")
result_temp.pack(pady=2)

result_humidity = tk.Label(root, text="", font=("Arial", 14), bg="#aee6ff")
result_humidity.pack(pady=2)

result_coord = tk.Label(root, text="", font=("Arial", 14), bg="#aee6ff")
result_coord.pack(pady=2)

root.mainloop()

      





                        