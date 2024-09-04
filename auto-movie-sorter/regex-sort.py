import re
import os

path_dir = "/media/hdd/trans-movie/download/complete"
name = os.listdir(path_dir) 
# print(os.listdir(path_dir))

title = name
pattern = r'^(.*?)\s*\('

for i in title:  
    try:
        match = re.search(pattern, i)
        if match:
            result = match.group(1)
            print(result)  # Output: Lord of War
    except:
        pass