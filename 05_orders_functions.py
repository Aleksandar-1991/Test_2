def calc_total_price(product: str, quantity: float):
    return {
        'coffee' : quantity * 1.50,
        'water' : quantity * 1.00,
        'coke' : quantity * 1.40,
        'snacks' : quantity * 2.00
    }.get(product, "Invalid product")

product=input()
quantity=float(input())

print(f"{calc_total_price(product, quantity):.2f}")