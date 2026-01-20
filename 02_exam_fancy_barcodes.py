import re

n = int(input())

expression = r'^\s*(\@\#+)([A-Z][A-Z-a-z0-9]{4,}[A-Z])\1\s*$'

for i in range(n):
    word = input()
    barcode = re.search(expression, word)
    prod_group = str()
    if barcode:
        prod_name = barcode[2]
        if prod_name.isalpha():
            prod_group = '00'
        else:
            for char in prod_name:
                if char.isdigit():
                    prod_group += char
        print(f"Product group: {prod_group}")
    else:
        print("Invalid barcode")

