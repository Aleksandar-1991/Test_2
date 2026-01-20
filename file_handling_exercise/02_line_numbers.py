import os

result = ""
with open("text.txt", "r") as file:

    lines = file.read().split("\n")
    for row, line in enumerate(lines):
        line_number = row + 1
        result += f"Line {line_number}: "
        letters = 0
        punctuation_marks = 0
        for char in line:
            if char.isalpha():
                letters +=1
            elif char in "-,.!?:\'\"":
                punctuation_marks += 1

        result += line + f" ({letters})({punctuation_marks})\n"


with open("output.txt", "w") as file:
    file.write(result )