## Overview

This is a simple implementation of the microservice architecture in Django and this repository runs along with https://github.com/baltonCome/Project Each repository complement the app.

### Installation

Clone the repository and in the same directory as '.env.example' create a '.env' configuration file and replace the environment variables with your own.


Move to Main>main directory


Run the docker-compose.yml file: ```docker-compose up --build```


in a separate terminal run: ```docker-compose exec backend sh```, to access the django app bash inside the container and run the migrations: ```python manage.py makemigrations``` and ```python manage.py migrate```


Note: You may need rerun the container after the migrations have finished, if necessary just rerun don't rebuild.

Note1: Wait for the app to connect to the RabbitMQ server before start testing.