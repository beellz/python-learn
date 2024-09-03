import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
movie_name = "lord%20of%20war"
year = "2005"

url = "https://api.themoviedb.org/3/search/movie?query=" + movie_name + "&language=en-US&page=1" + "&year=" + year

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + API_KEY
}

print(url)

response = requests.get(url, headers=headers)


print(response.text)