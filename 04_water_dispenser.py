from collections import deque

dispenser = int(input())

water_queue = deque()
while (name := input()) != "Start":
    water_queue.append(name)

while (command := input()) != 'End':
    if command.isdigit():
        person = water_queue.popleft()
        if int(command) <= dispenser:
            print(f"{person} got water")
            dispenser -= int(command)
        else:
            print(f"{person} must wait")
    else:
        tokens = command.split()
        liters = int(tokens[1])
        dispenser += liters

print(f"{dispenser} liters left")