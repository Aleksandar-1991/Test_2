import re
items = list()
total_cost = float()

expression = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while (command := input()) != 'Purchase':
    match = re.search(expression, command)
    if match:
        item, price, quantity = match.groups()
        total_cost += (float(price) * int(quantity))
        items.append(item)

print("Bought furniture:")
for itm in items:
    print(itm)
print(f"Total money spend: {total_cost:.2f}")
