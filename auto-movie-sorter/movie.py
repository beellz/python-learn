import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()

API_KEY = os.getenv("API_KEY_OMDB")

params = {
    # "movie_name":"lord of war",
    "t":"Dark",
    # "y":"2005"
    # "accept":"application/json",
    # "Authorization":"Bearer" + API_KEY
}

url = "http://www.omdbapi.com/?apikey=" + API_KEY
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer " + API_KEY
# }

response = requests.get(url, params=params)

print(response.url)
print(response.text)


json_data = response.json()

type = json_data['Type']
print(type)
