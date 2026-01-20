characters = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            for char in characters:
                line = line.replace(char, "@")
            print(" ".join(reversed(line.split())))