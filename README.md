# Anzere GIS Overhall
> This was a school project, part of the HES-SO Valais/Wallis Business-IT formation and more precisely, the GIS module. The goal was to learn how to model and display online a GIS interface. Our example was the Anzere ski resort.
> 
> You can find the final version of the project only on this Github. It is not deployed online.

<p align="center">
  <img width="600" height="auto" src="images/anzere-logo.png">
</p>

## Technologies Used
- HTML / CSS / JS
- PythonGIS / QGIS / PostGIS
- GeoPython
- Leaflet
- Docker

## Launced the application
- open a terminal or cmd and go under django
- run 'docker compose up'
- in docker, to the container web with the port 8000
- go to the terminal in this container and run 'bash'
- go under geoweb 'cd geoweb' and run 'python manage.py makemigrations' and then 'python manage.py migrate'
- populate the database 'python manage.py loaddata data.json'

You shoudl be able to access the website and the database with this configurations
