from string import punctuation

with open("text.txt", "r") as input_file, open("output.txt", "w") as output_file:
    result = ""

    for row, line in enumerate(input_file):
        letters = 0
        punctuation_marks = 0
        line = line.strip()
        for ch in line:
            if ch.isalpha():
                letters += 1
            elif ch in punctuation:
                punctuation_marks += 1
        result += f"Line {row + 1}: {line} ({letters})({punctuation_marks})\n"

    output_file.write(result)

