from collections import deque

n = int(input())
all_pumps = deque()

for i in range(n):
    data = input().split()
    petrol, distance = int(data[0]), int(data[1])
    all_pumps.append({'petrol': petrol, 'distance': distance})

rotations = 0

for i in range(n):
    fuel = 0
    for j in range(n):
        petrol, distance = all_pumps[j]['petrol'], all_pumps[j]['distance']
        fuel += petrol
        if fuel < distance:
            rotations += 1
            all_pumps.rotate(-1)
            fuel -= distance
            break
        fuel -= distance
    if fuel >= 0:
        print(rotations)
        break