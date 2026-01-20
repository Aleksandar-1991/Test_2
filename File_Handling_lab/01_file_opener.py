import os

path = os.path.join("..", "mydir", "weather_status.txt")

try:
    open(path, "r")
    print("File found")
except FileNotFoundError:
    print("File not found")