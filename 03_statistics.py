bakery = dict()

line = input()
while line != "statistics":
    tokens = line.split(": ")
    key = tokens[0]
    value = int(tokens[1])
    if key in bakery.keys():
        bakery[key] += value
    else:
        bakery[key] = value
    line = input()

print("Products in stock:")
for key,value in bakery.items():
    print(f"- {key}: {value}")

number_of_products = len(bakery.keys())
total_quantity = sum(bakery.values())
print(f"Total Products: {number_of_products}")
print(f"Total Quantity: {total_quantity}")

