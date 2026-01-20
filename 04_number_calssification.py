def positive(in_list: list) -> str:
    return ", ".join([str(number) for number in in_list if int(number)>=0])
def negative(in_list: list) -> str:
    return ", ".join([str(number) for number in in_list if int(number)<0])
def even(in_list: list) -> str:
    return ", ".join([str(number) for number in in_list if int(number)%2 == 0])
def odd(in_list: list) -> str:
    return ", ".join([str(number) for number in in_list if int(number)%2 != 0])


initial_list = list(map(int, input().split(", ")))

print(f"Positive: {positive(initial_list)}")
print(f"Negative: {negative(initial_list)}")
print(f"Even: {even(initial_list)}")
print(f"Odd: {odd(initial_list)}")