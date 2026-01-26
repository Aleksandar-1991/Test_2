def sum_nums(a, b):
    return a + b

def subtract_nums(a, b):
    return a - b

def multiply_nums(a, b):
    return a * b

def divide_nums(a, b):
    return a / b

def power_nums(a, b):
    return a ** b

mapper = {
    "+": sum_nums,
    "-": divide_nums,
    "*": multiply_nums,
    "/": divide_nums,
    "^": power_nums
}

def calculate(a, b, sign):
    return f"{mapper[sign](a, b):.2f}"