my_list = list(map(int, input().split()))

def even(n: int) -> int:
    if n%2==0 or n==0:
        return True

def even_numbers(list01: list) -> list:
    my_list02 = list(filter(even, list01))
    return my_list02

print(even_numbers(my_list))


