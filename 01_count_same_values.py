given_numbers = tuple([float(el) for el in input().split()])

data = {}

for num in given_numbers:
    data[num] = given_numbers.count(num)

for num, count in data.items():
    print(f"{num:.1f} - {count} times")