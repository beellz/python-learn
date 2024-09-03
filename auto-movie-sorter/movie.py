import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()

API_KEY = os.getenv("API_KEY")

params = {
    # "movie_name":"lord of war",
    "query":"lord of war",
    "include_adult":"false",   
    "language":"en-US",
    "page":"1",
    "year":"2005"
    # "accept":"application/json",
    # "Authorization":"Bearer" + API_KEY
}

url = "https://api.themoviedb.org/3/search/multi?"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + API_KEY
}

response = requests.get(url, params=params, headers=headers)

print(response.url)
# print(response.text)
# print("hello")
# print(response.json())
# print(response["title"])
#  json_data = response.json()


json_data = response.json()
# data = json.load(name)
# test = data.get("['results'][0]")

print(json_data)



