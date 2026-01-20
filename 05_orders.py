orders=int(input())
total_price=int()

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01>price_per_capsule or price_per_capsule>100.00:
        continue
    if (1 > days or days > 31):
            continue
    if 1>capsules_per_day or capsules_per_day>2000:
        continue
    price=price_per_capsule*capsules_per_day*days
    total_price+=price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")

