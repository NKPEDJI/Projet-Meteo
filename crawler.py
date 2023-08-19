import requests
import json
from cassandra.cluster import Cluster
import requests
import json
from cassandra.cluster import Cluster


#Conception de la base de données Cassandra:

#auth_provider = PlainTextAuthProvider(username='elastic', password='secret')

cluster = Cluster(contact_points=['172.17.0.5'], port=9042)
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
        City TEXT,
        temperature FLOAT,
        humidity FLOAT,
        speed FLOAT,
        description TEXT
    )
"""
session.execute(table_query)
# Fermeture de la session et du cluster
session.shutdown()
cluster.shutdown()