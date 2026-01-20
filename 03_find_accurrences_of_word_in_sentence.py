import re

text = input()
word = input()
expression = fr'\b{word}\b'

word_occurrences = re.findall(expression, text, re.IGNORECASE)

print(len(word_occurrences))