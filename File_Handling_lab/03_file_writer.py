import os
from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "my_first_file.txt")

with open(path, "w+") as file:
    # file.write('I just created my first file!')
    print(file.read())