import requests
from dotenv import load_dotenv
import os
import json
import shutil

load_dotenv()

API_KEY = os.getenv("API_KEY_OMDB")
path = '/home/beellz/workspace/python/python-learn/auto-movie-sorter/'
path_dir = "/home/beellz/workspace/python/python-learn/auto-movie-sorter/completed/"


all_files = "/all_files/"

folder_name = ["Movies", "Tv-series" ]

def file_creation():
    for i in folder_name:
        try:
            os.mkdir(path + all_files + i)
            print(f"Folder creating {i}")
        except FileExistsError:
            pass


name = os.listdir(path_dir)
# loop each name from path 
def sorter(name):
    for i in name:
        params = {"t":i}
        url = "http://www.omdbapi.com/?apikey=" + API_KEY
        response = requests.get(url, params=params)
        json_data = response.json()
        try:
            type = json_data['Type']
            year = json_data['Year']
            print(f"{i} is a {type} released on {year}")
            # get the each name and check if it movie or tv-series
            # move it according to the type
            if type == "movie":
                print(f"{i} is a movie and moving the folder in a movie folder")
                # dest = shutil.move(source, destination) 
                shutil.move(path_dir + i , path + all_files + "/Movies/" + i)
                # print(f"{path_dir}{i}")
                # print(f"{path}{all_files}/Movies/")
            elif type == "series":
                print(f"{i} is a tv series and moving to tv series folder")
                shutil.move(path_dir + i , path + all_files + "/Tv-series/" + i)
            else:  
                print("type unkonwn need to check in a different api") 
        except:
            pass

print(os.listdir(path_dir))

file_creation()
sorter(name)