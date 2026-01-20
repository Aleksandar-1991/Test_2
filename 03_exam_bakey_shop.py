stock_availability = dict()
sold = int()

while (input_line := input()) != 'Complete':
    command, quantity, food = input_line.split()
    quantity = int(quantity)
    if command == 'Receive':
        if food not in stock_availability.keys():
            stock_availability[food] = 0
        if quantity <= 0:
            continue
        else:
            stock_availability[food] += quantity
    elif command == 'Sell':
        if food not in stock_availability:
            print(f"You do not have any {food}.")
        else:
            if stock_availability[food] < quantity:
                quantity_needed = quantity - stock_availability[food]
                quantity_sold = stock_availability[food]
                stock_availability[food] = 0
                sold += quantity_sold
                del stock_availability[food]
                print(f"There aren't enough {food}. You sold the last {quantity_sold} of them.")
            else:
                stock_availability[food] -= quantity
                print(f"You sold {quantity} {food}.")
                sold += quantity
                if stock_availability[food] == 0:
                    del stock_availability[food]

for item, quantity in stock_availability.items():
    print(f"{item}: {quantity}")
print(f"All sold: {sold} goods")