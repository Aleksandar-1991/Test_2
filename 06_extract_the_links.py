import re

expression = r'((w{3})\.([A-Za-z0-9\-]+)(\.[a-z]+)+)'
while (command := input()) != "":
    matches = re.search(expression, command)
    if matches:
        link = matches.group(1)
        print(link)
