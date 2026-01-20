def calculate(operator: str, num01: int, num02: int):
    return {
        'multiply' : num01 * num02,
        'divide' : int(num01 / num02),
        'add' : num01 + num02,
        'subtract' : num01 - num02
    }.get(operator, "Invalid Operator")

operator = input()
num01, num02 = int(input()), int(input())

print(calculate(operator, num01, num02))