import re

line = input()
while line:
    expression = r'\d+'
    matches = re.findall(expression, line)
    if matches:
        print(' '.join(matches), end=' ')

    line = input()



