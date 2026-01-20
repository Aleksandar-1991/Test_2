import os
from constants import ABSOLUTE_PROJECT_PATH



try:
    path = os.path.join(ABSOLUTE_PROJECT_PATH, "my_first_file.txt")
    os.remove("my_first_file.txt")
except FileNotFoundError:
    print("File already deleted")