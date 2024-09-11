import requests
from datetime import datetime
# from dotenv import load_dotenv
import os
import json
import shutil

path_movie = '/media/hdd/trans-movie/download/Movies/'
path_tv = '/media/hdd/trans-movie/download/Series/'
path_anime = '/media/hdd/trans-movie/download/Anime/'
path_game = '/media/hdd/trans-movie/download/Game/'
path_books = '/media/hdd/trans-movie/download/Books/'
path_dir = "/media/hdd/trans-movie/download/complete/"


# name = input("please any movie or tv series name: ")
name = os.listdir(path_dir)

def sorter(name):
    for i in name:
        url = "http://34.100.225.108:11434/api/generate"
        payload = {
            "model": "llama2-uncensored",
            "prompt":"Give me one word response, is this a movie, anime, series and do not hallucinate, if you are not sure with the answer, response as not sure. " + i,
            "stream": False
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        json_data = response.json()
        type = json_data['response']
        print(type)

        print(f"{i} is a {type} ")
        source_path = os.path.join(path_dir, i)
        if type == "Movie":
            print(f"{type} is a movie and moving the folder to the movie folder")
            destination_path = os.path.join(path_movie, i)
            shutil.move(source_path, destination_path)
            print(f"Moved from {source_path} to {destination_path}")
        elif type == "Series" or type == "series" or type == "tv-series":
            # print(f"{type} is a TV series and moving to TV series folder")
            destination_path = os.path.join(path_tv, i)
            shutil.move(source_path, destination_path)
            print(f"Moved from {source_path} to {destination_path}")
        elif type == "Book":
            # print(f"{type} is a TV series and moving to TV series folder")
            destination_path = os.path.join(path_books, i)
            shutil.move(source_path, destination_path)
            print(f"Moved from {source_path} to {destination_path}")
        elif type == "Anime":
            # print(f"{type} is a TV series and moving to TV series folder")
            destination_path = os.path.join(path_anime, i)
            shutil.move(source_path, destination_path)
            print(f"Moved from {source_path} to {destination_path}")
        elif type == "Game":
            # print(f"{type} is a TV series and moving to TV series folder")
            destination_path = os.path.join(path_game, i)
            shutil.move(source_path, destination_path)
            print(f"Moved from {source_path} to {destination_path}")
        else:
            print(type)
            print("Type unknown, need to check in a different API")

print(name)
sorter(name)            

current_dateTime = datetime.now()
print()
print("last Completed setup was on")
print(current_dateTime)
print()
print()
print()


# curl request using LLM
# curl http://34.100.225.108:11434/api/generate -d '{
#   "model": "llama2-uncensored",
#   "prompt":"Give me one word response, is this a movie, anime, series and dont hallucinate, if answer doesnt know response as don't know. Tomorrowland 2015",
#   "stream" : false
# }'