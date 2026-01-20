from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))
milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    elif chocolates[-1] <= 0:
        chocolates.pop()
        continue
    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        chocolates[-1] -= 5
        cups_of_milk.rotate(-1)

print(f"Great! You made all the chocolate milkshakes needed!" if milkshakes >= 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) if cups_of_milk else 'empty'}")
