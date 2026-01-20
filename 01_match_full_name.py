import re

text = input()

expression = r'\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b'

numbers = re.findall(expression, text)


print(', '.join(numbers))
