# ProjetMeteo
L'objectif de ce projet est de construire une plateforme automatisée qui utilise Python pour le web 
scraping d'informations météorologiques de la France depuis une API Open Data, puis stocke ces 
informations dans une base de données Cassandra. Le tout sera encapsulé et orchestré à l'aide de 
Docker et Docker Compose pour assurer une mise en production fluide et scalable.

# Installation et Configuration 

- docker , docker compose , python , ubuntu


- creation d'un dossier dans ubuntu que nous avons nommé : "ProjetMeteo" 
- Dans ce dossier nous avons crée les fichiers :
    . crawler.py qui contient le code python 
    . requierements.txt qui contient les bibliothèques à installer
    . docker-compose.yml : service pour lancer docker-compose
    . dockerfile : service pour éxecuter le projet

    et un sous dossier nommé: "cassandra" qui contient le fichier :
    .Dockerfile : code du service de cassandra

- Dezipper dans le dossier ProjetMeteo le fichier  city.json qui se trouve a ce lien
http://bulk.openweathermap.org/sample/city.list.json.gz


# Utilisation

- Modifier dans le fichier crawler.py à la ligne 20 l' API_KEY = "399395db781052ed64fd8577e1b39fa0" par votre  api_key que vous obtenez sur le site 
https://openweathermap.org/  => dans le menu compte =>  onglet mon api key

- Une fois l'api key modifier , enregistrer le fichier avec CTRL S 

- Build le projet en vous positionnant sur la racine de votre projet et en tapant la commande :
    . docker-compose build  : construire l'image docker
    . docker-compose up : pour éxecuter le projet

- Une fois le projet éxéctuer avec succès:    
    . ouvrez un autre terminal et positionner vous sur le ProjetMeteo et tapez la commande docker ps 
    . Cette commande vous affichera l'ID CONTAINER de l'image cassandra ; copier cet ID
    . Executer ensuite la commande : sudo docker exec -it IDCASSANDRA /bin/bash   (vous remplacerez IDCASSANDRA par ID container de cassandra que vous avez précedemment copier)
    . Tapez ensuite la commande :  cqlsh  => pour se connecter à cassandra
    . Une fois connectez visualisez vos données avec la requête :  select * from weather_keyspace.weather_data ;


# Membres:
Projet réalisé par :
- N KPEDJI Florence
- GUERARD Valentin
-  ALLAH ASRA BADJINAN Gaëtan
- Mohamed Rachidy RACHDA