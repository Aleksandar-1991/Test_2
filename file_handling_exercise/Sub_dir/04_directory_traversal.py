import os

files = {}

start_directory = "../"

def get_files(directory, level):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(item)
        else:
            get_files(item_path, level - 1)

get_files(start_directory, 1)

with open("output.txt", "w") as output_file:
    for key, values in sorted(files.items()):
        output_file.write(f"{key}\n")
        for value in sorted(values):
            output_file.write(f"- - - {value}\n")