num = int(input())

def calc_factorial(n):
    if n == 1:
        return n

    return n*(calc_factorial(n-1))

print(calc_factorial(num))