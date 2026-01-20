from collections import deque

text = input().split()

operators = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a // b)
}

numbers = deque()

for item in text:
    if item not in "+-*/":
        numbers.append(int(item))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            numbers.appendleft(operators[item](first_number, second_number))

print(numbers[0])