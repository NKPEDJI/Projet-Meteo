import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "http://api.openweathermap.org/"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Pour obtenir les températures en Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        #print(f"Weather in {city_name}:")
        #print(f"Description: {weather_description}")
        #print(f"Temperature: {temperature}°C")
        #print(f"Humidity: {humidity}%")
        #print(f"Wind Speed: {wind_speed} m/s")

        weather_data = {
            "City": city_name,
            "Description": weather_description,
            "Temperature": temperature,
            "Humidity": humidity,
            "Wind Speed": wind_speed
        }
         return weather_data

    else:
        print("Error fetching weather data")

if __name__ == "__main__":
    city_name = "Paris"  # Nom de la ville pour laquelle vous souhaitez obtenir les informations météorologiques
    #get_weather(city_name)
        weather_info = get_weather(city_name)

    if weather_info:
        print("Weather Information:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
