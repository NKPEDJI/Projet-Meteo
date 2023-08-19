import requests
import json

API_KEY = "cbedf9374cc81594a05d3ed33264416a"


# URL de l'API pour les informations météorologiques
#API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"


# Chargement des données des villes depuis le fichier city.list.json
with open("city.list.json", "r", encoding="utf-8") as json_file:
    city_data = json.load(json_file)

# Liste pour stocker les informations météorologiques des villes de France
weather_data = []

# Boucle à travers les villes
for city in city_data:
    if city["country"] == "FR": 
        #print("condition france validé") # Filtrer les villes de France
        city_name = city["name"]
        #print(city_name)
        city_id = city["id"]

        API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

        # Paramètres pour l'appel à l'API
        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric" 
        }

        # Appel à l'API
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            #print("appel api reussi")

            # Extraction des informations pertinentes
            weather_info = {
                "city_name": city_name,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "weather_description": data["weather"][0]["description"]               
            }
            print("infos pertinents reussi")

            # Ajout des informations à la liste
            weather_data.append(weather_info)
            #print(weather_data)

# Affichage des informations météorologiques
for info in weather_data:
    print(f"City: {info['city_name']}")
    print(f"Temperature: {info['temperature']} C")
    print(f"Humidity: {info['humidity']}")
    print(f"wind_speed: {info['wind_speed']}")
    print(f"Weather Description: {info['weather_description']}")
    print("-" * 30)
    print("méteo")

 