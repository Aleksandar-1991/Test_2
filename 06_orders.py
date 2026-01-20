products = dict()

while (command := input()) != 'buy':
    name, price, quantity = command.split()
    if name not in products.keys():
        products[name] = [price, int(quantity)]
    else:
        if products[name][0] != price:
            products[name][0] = price
        products[name][1] += int(quantity)

for name, details in products.items():
    total_price = float(details[0]) * int(details[1])
    print(f"{name} -> {total_price:.2f}")

