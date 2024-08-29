# create all folder for different types

import os 
import shutil

path = '/home/beellz/workspace/python/python-learn/auto-file-mover/all_files/'
folder_name = ["images", "videos", "music", "text", "pdf", "screenshot" ]

def file_creation():
    for i in folder_name:
        try:
            os.mkdir(path + i)
            print(f"Folder creating {i}")
        except FileExistsError:
            print(f"Folder already exisits {i}")

# Find the image file
# get all of them in a list  
# move all the folder on spefic folder 



print(os.listdir(path))

def move_files():
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            shutil.move(path + filename, path + "images/" + filename)
            print(f"moving {filename} to the images folder")
        elif filename.endswith(".png"):
            shutil.move(path + filename, path + "screenshot/" + filename)
            print(f"moving {filename} to the screenshot folder")
        elif filename.endswith(".mv"):
            shutil.move(path + filename, path + "videos/" + filename)
            print(f"moving {filename} to the videos folder")
        elif filename.endswith(".mp3"):
            shutil.move(path + filename, path + "music/" + filename)
            print(f"moving {filename} to the music folder")
        elif filename.endswith(".txt"):
            shutil.move(path + filename, path + "text/" + filename)
            print(f"moving {filename} to the text folder")
        elif filename.endswith(".pdf"):
            shutil.move(path + filename, path + "pdf/" + filename)
            print(f"moving {filename} to the pdf folder")
        elif filename.endswith(".mp4"):
            shutil.move(path + filename, path + "videos/" + filename)
            print(f"moving {filename} to the videos folder")
        elif os.path.isdir(path + filename):
            print(f"{filename} is a folder")
        else:
            print(f"{filename} cannot catagorised")

file_creation()
move_files()
