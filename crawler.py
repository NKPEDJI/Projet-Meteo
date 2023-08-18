import requests

API_KEY = "cbedf9374cc81594a05d3ed33264416a"
city_name = "Paris"
BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # To get temperatures in Celsius
    }

    response = requests.get(BASE_URL, params=params)
    print("get response")
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()

        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

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
    city_name = "Paris"
    weather_info = get_weather(city_name)

    if weather_info:
        print("Weather Information:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
