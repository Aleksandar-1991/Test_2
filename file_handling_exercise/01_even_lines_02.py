import re

with open("text.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        line = reversed(re.sub("[-,.!?]", "@", lines[i]).split())
        print(*line)
