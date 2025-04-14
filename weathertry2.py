from datetime import datetime

def get_weather(city):
    params = {
        "q": city,
        "appid": "API_KEY", #apikey
        "units": "metric"
    }
    response = requests.get("BASE_URL", params=params) #url
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_description = data["weather"][0]["description"]

        # Hora local del lugar (necesita timestamp + zona horaria en segundos)
        timestamp = data["dt"]
        timezone_offset = data["timezone"]
        local_time = datetime.utcfromtimestamp(timestamp + timezone_offset).strftime('%Y-%m-%d %H:%M:%S')

        print(f"\nWeather in {city_name}:")
        print(f"- Description: {weather_description.capitalize()}")
        print(f"- Temperature: {temperature}°C (feels like {feels_like}°C)")
        print(f"- Humidity: {humidity}%")
        print(f"- Wind Speed: {wind_speed} m/s")
        print(f"- Local Time: {local_time}")
    else:
        print("City not found. Please try again.")
