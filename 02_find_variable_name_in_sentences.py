import re

text = input()

expression = r'\b_([A-Za-z0-9]+)\b'

variables = re.findall(expression, text)

print(','.join(variables))