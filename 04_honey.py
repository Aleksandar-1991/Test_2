from collections import deque

bees = deque(map(int, input().split()))
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees and nectar:
    if bees[0] <= nectar[-1]:
        honey += abs(operators[symbols[0]](bees.popleft(), nectar.pop()))
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
print(f"Bees left: {', '.join(str(x) for x in bees)}") if bees else None
print(f"Nectar left: {', '.join(str(x) for x in nectar)}") if nectar else None