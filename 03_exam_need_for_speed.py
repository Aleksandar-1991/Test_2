from importlib.metadata import pass_none

n = int(input())

cars = dict()
for i in range(n):
    tokens = input().split('|')
    car, mileage, fuel = tokens[0], int(tokens[1]), int(tokens[2])
    cars[car] = {'mileage': mileage, 'fuel': fuel}

while (input_line := input()) != 'Stop':
    tokens = input_line.split(" : ")
    command = tokens[0]
    if command == 'Drive':
        car, distance, fuel = tokens[1], int(tokens[2]), int(tokens[3])
        if cars[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
            continue
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['mileage'] > 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif command == 'Refuel':
        car, fuel = tokens[1], int(tokens[2])
        fuel_needed = 75 - cars[car]['fuel']
        if fuel_needed < fuel:
            cars[car]['fuel'] = 75
            print(f"{car} refueled with {fuel_needed} liters")
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        car, kilometers = tokens[1], int(tokens[2])
        if cars[car]['mileage'] - kilometers < 10000:
            cars[car]['mileage'] = 10000
        else:
            cars[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")

