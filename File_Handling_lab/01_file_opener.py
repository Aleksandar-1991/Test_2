from constants import ABSOLUTE_PROJECT_PATH
import os

path = os.path.join(ABSOLUTE_PROJECT_PATH, "..", "mydir", "weather_status.txt")

try:
    open(path, "r")
    print("File found")
except FileNotFoundError:
    print("File not found")
