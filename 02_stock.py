elements = input().split()
stock_needed = input().split()

bakery = dict()

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    bakery[key]=int(value)

for item in stock_needed:
    if item in bakery.keys():
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

