num01 = int(input())
num02 = int(input())

def factorial(n: int) -> int:
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

def factorial_division(a: int, b: int) -> float:
    fac_a=factorial(a)
    fac_b=factorial(b)
    return fac_a/fac_b

print(f"{factorial_division(num01, num02):.2f}")