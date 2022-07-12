from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Route for "/" (frontend):
@app.route('/')
def index():
  return render_template("index.html")


# Route for "/MIX" (middleware):
@app.route('/MIX', methods=["POST"])
def POST_weather():
  #take in and format location data
  #coordinates: 40.1125,-88.2284
  location = request.form["location"]
  data = {}

  #check if valid lat and long(does comma separate)
  if len(location.split(',')) != 2:
    return "Malformed request..", 400

  lat, lng = location.split(',')

  #google map API call
  key = 'AIzaSyA1LJO0NZWKLOBfdVShtFOS6Q8BHAcBXEU'
  locationinfo = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&result_type=locality&sensor=false&key={key}")
  locationData = locationinfo.json()

  #caching
  locationinfo.headers['Cache-Control'] = 'public, max-age=86400'
  locationinfo.headers['Age'] = 0
  locationinfo.headers.get('Cache-Control')
  print(locationinfo.headers)
  

  #check if valid lat and long(does it exist)
  if locationData["status"] == "INVALID_REQUEST":
    data = locationData["error_message"]
    return data, 400

  #check if valid lat and long(any results)
  if locationData["status"] == "ZERO_RESULTS":
    return "Middle of nowhere", 400

  #retrieves state and city from API
  data["State"] = locationData["results"][0]["address_components"][-2]["long_name"]

  data["City"] = locationData["results"][0]["address_components"][0]["long_name"]


  #interface with population microservice
  pop_url = os.getenv('POPULATION_MICROSERVICE_URL')
  r = requests.get(f'{pop_url}/{data["State"]}/')
  pop_data = r.json()

  #interface with timezone microservice
  timezone_url = os.getenv('TIMEZONE_MICROSERVICE_URL')
  rt = requests.get(f'{timezone_url}/{data["City"]}/{lat}/{lng}/')
  timezone_data = rt.json()

  #interface with datetime microservice
  datetime_url = os.getenv('DATETIME_MICROSERVICE_URL')
  rj = requests.get(f'{datetime_url}/{timezone_data}')
  datetime_data = rj.json()


  #interface with weather microservice
  weather_url = os.getenv('WEATHER_MICROSERVICE_URL')
  re = requests.get(f'{weather_url}/{data["City"]}/')
  weather_data = re.json()

  #interface with zipcode microservice
  zipcode_url = os.getenv('ZIPCODE_MICROSERVICE_URL')
  z = requests.get(f'{zipcode_url}/{data["City"]}/')
  zipcode_data = z.json()

  #interface with city microservice
  city_url = os.getenv('CITY_MICROSERVICE_URL')
  city = requests.get(f'{city_url}/{data["City"]}/')
  city_data = city.json()

  #interface with senator microservice
  # @TO-DO: Fix query to input state shortname (take in IL not Illinois)
  senator_url = os.getenv('SENATOR_MICROSERVICE_URL')
  senator = requests.get(f'{senator_url}/{data["State"]}/')
  senator_data = senator.json()

  #interface with senator microservice
  # @TO-DO: Fix query to input state shortname (take in IL not Illinois)
  rep_url = os.getenv('REP_MICROSERVICE_URL')
  rep = requests.get(f'{rep_url}/{data["State"]}/')
  rep_data = rep.json()
  

  if r.status_code == 404:
   data = pop_data["error"]
   return data, 400

  #list of microservices. PUT IN THIS LIST FOR OUTPUT
  microservice_list = [pop_data, datetime_data, "Time zone: " + timezone_data]
  weather_list = [weather_data]
  zipcode_list = [zipcode_data]
  city_list = [city_data]

  return jsonify(microservice_list, weather_list, zipcode_list, city_list), 200

  