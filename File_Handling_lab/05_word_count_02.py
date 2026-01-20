import os
import re
from constants import ABSOLUTE_PROJECT_PATH


with open(os.path.join(ABSOLUTE_PROJECT_PATH, "words.txt"), "r") as file:
    words = [word for word in file.read().split()]

with open(os.path.join(ABSOLUTE_PROJECT_PATH, "input.txt"), "r") as file:
    text = file.read()

result = {}

for word in words:
    expression = rf"\b{word}\b"
    matched_words = re.findall(expression, text, re.IGNORECASE)
    result[word] = len(matched_words)

sorted_result = sorted(result.items(), key= lambda kvp: -kvp[1])

with open(os.path.join(ABSOLUTE_PROJECT_PATH, "output.txt"), "w") as file:
    for key, value in sorted_result:
        file.write(f"{key} - {value}\n")