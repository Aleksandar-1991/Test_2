from collections import deque

food_quantity = int(input())

servings = deque(map(int, input().split()))

print(max(servings))
for i in range(len(servings)):
    order = servings[0]
    if order <= food_quantity:
        food_quantity -= order
        servings.popleft()
    else:
        break

if servings:
    print(f"Orders left: {' '.join([str(x) for x in servings])}")
else:
    print('Orders complete')

