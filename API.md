# Project MIX: API Documentation

## Overview of Implementation 
Our implementation of the MIX middleware utilizes the ``Google Maps API`` to retrieve the address of the coordinates that are inputted in the ``Location:`` field, whilst error checking any invalid lat/long inputs that returns an error message to the user. Once the geolocation coordinates are inputted, both of our implemented IMs are called that will take the information from the geolocation coordinates and retrieve information such as the state population and weather for that specific location.

Our file structure consists of a main ``app.py`` that contains our middleware for our application and two directories for our information microservices: ``population-microservice`` that returns the state’s population and ``weather-microservice`` that returns the city’s geolocation coordinates and gives the forecast from that particular location. Our application runs on 3 different ports. Two of our ports for our microservices can be found in ``.env``

## Demonstration of MIX
![Alt Text](https://media.giphy.com/media/vy5eBTnyuGxhvJyZsE/giphy.gif)

## Technical Specification
Our middleware utilizes the ``Google Maps API`` to retrieve the geolocation coordinates as mentioned earlier. We also used the ``Census API`` and ``OpenWeather API`` for both of our information microservices that is further explained in ``IMs.md``

## Running our MIX Service
### Note: We expanded our IM development in order to work for the Coursewide Microservice in Week 3 and 4
To run our MIX service, you need to clone our repository to your local machine using the command ``https://github.com/cs240-illinois/cs240-fa21-MIX_Team-Flask-mpara3-jkim758.git``. Once the repository is retrieved, you are able to access the files from your IDE (we recommend VSCode). Make sure to ``cd`` to our folder directory. From there, you will need to run 3 different servers locally at the same time. 

To run the entire application, ``cd`` to the main folder directory and run the command ``flask run``. Once you run the command, you will see ``​​Running on http://127.0.0.1:5000/ `` where you can navigate to the given URL. However, we need to run two of our information microservices in order for the middleware to work properly. 

The next step would be to open another terminal and ``cd population-microservice`` and run the command ``flask run`` to run the population microservice. To know it’s running, it will return ``Running on http://127.0.0.1:24000/`` to the terminal. 

The last step would be to, again, open another terminal and ``cd weather-microservice`` and run the command ``flask run`` to run the population microservice. To know it’s running, it will return ``Running on http://127.0.0.1:25000/`` to the terminal. 

Once all the services are running, go on a browser to ``http://127.0.0.1:5000/`` to access the middleware and input the location as ``40.1125,-88.2284`` that will return output for population and forecast from the 2 information microservices.