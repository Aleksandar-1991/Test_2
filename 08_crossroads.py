from collections import deque

green_light = int(input())
free_window = int(input())
car_queue = deque()
cars_passed = 0
car_crash = False
crash_part = str()

while (command := input()) != 'END':
    if command != 'green':
        car_queue.append(command)
    elif command == 'green':
        current_green = green_light
        while car_queue and current_green > 0 :
            current_car = car_queue[0]
            if len(current_car) <= current_green:
                current_green -= len(current_car)
                car_queue.popleft()
                cars_passed += 1
            else:
                break
        if not car_queue:
            continue
        current_car = car_queue[0]
        if ( current_green + free_window) - len(current_car) >= 0:
            cars_passed += 1
        else:
            passing_car_part = current_green + free_window
            crash_part = current_car[passing_car_part]
            break
        car_queue = deque()

if not crash_part:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
else:
    print("A crash happened!")
    print(f"{car_queue[0]} was hit at {crash_part}.")

