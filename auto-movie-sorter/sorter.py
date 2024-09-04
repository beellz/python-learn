import requests
from dotenv import load_dotenv
import os
import json
import shutil
import re

load_dotenv()

API_KEY = os.getenv("API_KEY_OMDB")
path_movie = '/media/hdd/Movies/'
path_tv = '/media/hdd/TV-series/'
path_dir = "/media/hdd/trans-movie/download/complete"

pattern = r'^(.*?)\s*\('

def sorter(name):
    for i in name:
        try:
            match = re.search(pattern, i)
            if match:
                result = match.group(1).strip()
            print(result)
            params = {"t": result}
            url = "http://www.omdbapi.com/?apikey=" + API_KEY
            response = requests.get(url, params=params)
            json_data = response.json()
            
            try:
                type = json_data['Type']
                year = json_data['Year']
                print(f"{result} is a {type} released on {year}")
                
                source_path = os.path.join(path_dir, i)
                
                if type == "movie":
                    print(f"{result} is a movie and moving the folder to the movie folder")
                    destination_path = os.path.join(path_movie, i)
                    shutil.move(source_path, destination_path)
                    print(f"Moved from {source_path} to {destination_path}")
                elif type == "series":
                    print(f"{result} is a TV series and moving to TV series folder")
                    destination_path = os.path.join(path_tv, i)
                    shutil.move(source_path, destination_path)
                    print(f"Moved from {source_path} to {destination_path}")
                else:
                    print("Type unknown, need to check in a different API")
            except KeyError:
                print(f"Error: Unable to determine type for {result}")
        except Exception as e:
            print(f"Error processing {i}: {str(e)}")

name = os.listdir(path_dir)
print("Files in source directory:", name)

sorter(name)