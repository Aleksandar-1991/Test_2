n = int(input())
cars = set()
for i in range(n):
    data = input().split(", ")
    direction, reg_number = data[0], data[1]
    if direction == 'IN':
        cars.add(reg_number)
    else:
        cars.remove(reg_number)

if cars:
    print(*cars, sep='\n')
else:
    print("Parking Lot is Empty")