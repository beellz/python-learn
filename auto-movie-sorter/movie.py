import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://api.themoviedb.org/3/search/movie?query=lord%20of%20war&include_adult=true&language=en-US&page=1&year=2005"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + API_KEY
}
# eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZWVmZDM1M2QyMDMyODIyYjY2N2MyZjIxYTk4MzhjZSIsIm5iZiI6MTcyNTM2MjQwMi4zMjk2MDQsInN1YiI6IjY0ODJmM2YwYmYzMWYyNTA1NWEwMDRkMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3E79yFNPfphQVI3gxZarBy2s8mCoCVRvOF5FHRRGUug
response = requests.get(url, headers=headers)

print(API_KEY)

print(response.text)