# Imports
from flask import Flask, render_template
from flask import request, jsonify
from dotenv import load_dotenv
import os
import requests


# Initiating app
load_dotenv()  # loading env variables
app = Flask(__name__)  # initiating Flask as app
app.config.update(
    DEBUG=True
)


# Using dotenv to hide the API key
API_KEY = os.environ.get("API_KEY")
# Url where the api is located
url = "https://community-open-weather-map.p.rapidapi.com/weather"
# Needed headers to get the data from the api
headers = {
    'x-rapidapi-key': API_KEY,  # testing the api replace with your own key
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",  # api host
}


# Get function to get and parse the data from the api
def get_data(city, country):
    # The api need the city capitalized and country to be lowercase.
    # To prefent errors from happening forcing the url to behave like this.
    city = city.lower().capitalize()
    country = country.lower()
    qstring = {"q": f"{city},{country}"}
    response = requests.request("GET", url, headers=headers, params=qstring)
    return response.json()


# Home route to see on the default homepage
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', name=home)


# API get route
@app.route('/api/v1/weather/<city>/<country>', methods=['GET'])
def api_get_weather(city, country):
    return get_data(city, country)


# Main function to run
if __name__ == '__main__':
    app.run()
