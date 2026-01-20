import re

text = input()
expression = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'

destinations = list()

temp_dest= re.findall(expression, text)

for dest in temp_dest:
    destinations.append(dest[1])

print(f"Destinations: {', '.join(destinations)}")
destinations_length = int()
for d in destinations:
    destinations_length += len(d)
print(f"Travel Points: {destinations_length}")




