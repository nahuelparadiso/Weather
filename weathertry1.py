import requests

API_KEY = "enter ur api key"  # Enter your API key, you can find it in the link (create account)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {city_name}: {weather_description.capitalize()}, {temperature}°C")
    else:
        print("City not found. Please try again.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
