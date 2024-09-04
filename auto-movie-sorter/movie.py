import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()

API_KEY = os.getenv("API_KEY_OMDB")

name = input("please any movie or tv series name: ")

params = {
    # "movie_name":"lord of war",
    "t":name
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

try:
    type = json_data['Type']
    year = json_data['Year']
    print(f"{name} is a {type} released on {year}")
except:
    print("not movie or tv series")