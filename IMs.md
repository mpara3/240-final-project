# Project MIX: Information Microservices Documentation

For our implementation, we developed 9 IMs : a ``population-microservice``, ``weather-microservice``, ``zipcode-microservice``, ``city-microservice``, ``dateime-microservice``, ``timezone-microservice``, ``location-microservice``, ``senator-microservice``, ``rep-microservice``

## Jishan's IMs

* For the ``Population IM``, it took in the state of the parameter and iterated through a list of state values. If the state value matched the state provided, it would return the state population. This used the ``Census API``, which took in a state and returned the population. to reiterate, it gets state population based off recent data

* For the ``Timezone IM``, it takes in the city, and geocoodinates in order to get the timezome from that specific region using the ``Google Maps API.`` 

* For the ``Datetime IM``, it takes in the city, and country in order to get the time from that specific region using the. 

## Monica's IMs

* For the ``Weather IM``, it takes in the city parameter and returns the forecast of the city with its output of coordinate, temperature (in Kelvin, sadly), and humidity. The information for the weather comes from the ``OpenWeather API``

* For ``Senator IM`` it takes in a ``State Abbreviation`` and returns all the senators within that given state

* For ``Rep IM`` it takes in a ``State Abbreviation`` and returns all the State Representatives from a given state

* For ``Location IM`` it takes in the geocoordinates then converts them to either a ``City``, ``State``, or ``State Abbreviation`` query so that the other IMs can depend on the information for the coursewide microservice. 