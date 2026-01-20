import re

text = input()

expression = r'\s([a-z0-9]+[a-z0-9\.\-\_][a-z0-9]+@([a-z]+[a-z\-]+[a-z]+)(\.[a-z]+)+)\b'


email_addresses = re.findall(expression, text)

for mail in email_addresses:
    print(mail[0])


