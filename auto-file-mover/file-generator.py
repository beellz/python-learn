import os
 
# path of the current script
path = '/home/beellz/workspace/python/python-learn/auto-file-mover/'
 
# Before creating
dir_list = os.listdir(path)
print("List of directories and files before creation:")
print(dir_list)
print()

path_dir = './all_files'

# Create the directory
try:
    os.mkdir(path_dir)
    print("Directory created successfully!")
except FileExistsError:
    print("Directory already exists.")
main_dir = path + path_dir

# Creating a file at specified location

file_ext = ["txt", "pdf" , "mp3" , "mp4" , "jpg", "png", "mv"]


for i, ext in zip(range(1, 10), file_ext):
    for ext in file_ext:
        print(main_dir, 'myfile' + str(i) + '.' + ext)
        with open(os.path.join(main_dir, 'myfile' + str(i) + '.' + ext), 'w') as fp:
            pass


# initally thought of this way to write each extenstion
# then figured out that it can be simply loop

# for name, age in zip(names, ages):
#     print(name, "is", age, "years old.")

# for i in range(1, 10):
#     with open(os.path.join(main_dir, 'myfile' + str(i) + '.txt'), 'w') as fp:
#         pass
#     with open(os.path.join(main_dir, 'jobscan' + str(i) + '.pdf'), 'w') as fp:
#         pass
#     with open(os.path.join(main_dir, 'listing' + str(i) + '.mp3'), 'w') as fp:
#         pass
#     with open(os.path.join(main_dir, 'video' + str(i) + '.mp4'), 'w') as fp:
#         pass
#     with open(os.path.join(main_dir, 'image' + str(i) + '.jpg'), 'w') as fp:
#         pass
#     with open(os.path.join(main_dir, 'movie' + str(i) + '.mv'), 'w') as fp:
#         pass


dir_list_new = os.listdir(main_dir)
print(dir_list_new)

