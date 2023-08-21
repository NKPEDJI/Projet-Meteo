import requests
import json
from cassandra.cluster import Cluster
import time
import urllib.parse
from decimal import Decimal

import logging

# Configuration du logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


#----1. Recherche et Sélection d'API
#https://openweathermap.org/
#2.---- Configuration de l'environnement de développement: fait 
#----3. Développement du script Python----

API_KEY = "399395db781052ed64fd8577e1b39fa0" #-- à remplacer par votre api_key
# Chargement des données des villes depuis le fichier city.list.json
with open("city2.list.json", "r", encoding="utf-8") as json_file:
    city_data = json.load(json_file)


# Liste pour stocker les informations météorologiques des villes de France
weather_data = []


# Fonction pour les appels à l'API
def fetch_weather_data(city_name):
    try:
        API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Lève une exception si la requête a échoué
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de l'appel à l'API pour la ville {city_name}: {e}")
        return None



# Boucle à travers les villes
for city in city_data:
    if city["country"] == "FR":  # Filtrer les villes de France
        city_name = city["name"]
        city_id = city["id"]
        # Encodage du nom de la ville pour gérer les caractères spéciaux
        encoded_city_name = urllib.parse.quote(city_name)

        #API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
        # Paramètres pour l'appel à l'API
        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric"
        }
        # Appel à l'API avec gestion des erreurs
        weather_response = fetch_weather_data(encoded_city_name)
        #print(response.status_code)

        if weather_response is not None:
            data = weather_response

            # Extraction des informations pertinentes
            weather_info = {
                "city_id": city_id,
                "city_name": city_name,
                "humidity": data["main"]["humidity"],
                "temperature": data["main"]["temp"],
                "weather_description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }

            # Ajout des informations à la liste
            weather_data.append(weather_info)
            # Introduire un délai de 2 secondes entre les requêtes
            time.sleep(2)
    

# Affichage des informations météorologiques
#for info in weather_data:
#    print("Méteo")
#    print(f"City_id: {info['city_id']}")
#    print(f"City: {info['city_name']}")
#    print(f"Temperature: {info['temperature']} °C")
#    print(f"Humidity: {info['humidity']}")
#    print(f"wind_speed: {info['wind_speed']}")
#    print(f"Weather Description: {info['weather_description']}")
#    print("-" * 30)


print("Cassandra")
#----4.Conception de la base de données Cassandra:----
cluster = Cluster(contact_points=['cassandra'], port=9042)
# Connection au cluster et creation de session 
session = cluster.connect()
#Creation du keyspace
keyspace_stmt = "CREATE KEYSPACE IF NOT EXISTS weather_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}"
session.execute(keyspace_stmt)

# Utilisation du keyspace
session.set_keyspace('weather_keyspace')

# Création du schéma de la table
table_query = """

    CREATE TABLE IF NOT EXISTS weather_data (
        city_id INT PRIMARY KEY,
        city_name TEXT,
        humidity INT,
        temperature FLOAT,
        weather_description TEXT,
        wind_speed FLOAT
        
    )
"""
session.execute(table_query)


#----5. Intégration avec Cassandra en Python:----
# Préparation de la requête d'insertion


# Insertion des données dans la table
for info in weather_data:
    print(info)
    try:
    

        insert_query = f"""
            INSERT INTO weather_keyspace.weather_data (city_id, city_name, humidity, temperature, weather_description, wind_speed)
            VALUES ({info['city_id']}, '{info['city_name']}', {info['humidity']}, {info['temperature']}, '{info['weather_description']}', {info['wind_speed']})
        """
        session.execute(insert_query)

    except Exception as e:
        logger.error(f"Erreur lors de l'insertion des données pour la ville {info['city_name']}: {e}")

# Fermeture de la session et du cluster
session.shutdown()
cluster.shutdown()
