from collections import deque

food_quantity = int(input())

food_queue = deque(int(x) for x in input().split())
print(max(food_queue))
while food_queue and food_queue[0] <= food_quantity:
    food_quantity -= food_queue.popleft()

if food_queue:
    print("Orders left:", * food_queue)
else:
    print("Orders complete")