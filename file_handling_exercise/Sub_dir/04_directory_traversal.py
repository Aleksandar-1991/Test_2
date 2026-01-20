import os

files = {}

location = "../"

def get_files(directory, level):
    if level == -1: return

    for item in os.listdir(directory):
        path = os.path.join(location, item)
        if os.path.isfile(path):
            ext = os.path.splitext(item)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(item)
        else:
            print(path)
            get_files(path, level - 1)




get_files(location, 1)

with open("output.txt", "w") as output_file:
    for key, values in sorted(files.items()):
        output_file.write(f"{key}\n")
        for value in sorted(values):
            output_file.write(f"- - - {value}\n")