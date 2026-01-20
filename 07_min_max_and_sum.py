list01 = list(map(int, input().split()))

def min_max_and_sum(list02: list) -> int:
    min_num = min(list02)
    max_num = max(list02)
    sum_num = sum(list02)
    return min_num, max_num, sum_num

my_min, my_max, my_sum = min_max_and_sum(list01)
print(f"The minimum number is {my_min}")
print(f"The maximum number is {my_max}")
print(f"The sum number is: {my_sum}")