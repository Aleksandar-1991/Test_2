import math

int_list = list(map(int, input().split(', ')))
factor = int()
max_num = max(int_list)

def check_num_for_factor(lst: list, fct: int) -> str:
    my_list = []
    for num in lst:
        if (num - ((fct-1) * 10) <= 10) and (num - ((fct-1) * 10) >= 0):
            my_list.append(num)

    return f"Group of {fct*10}'s: {my_list}"


if max_num % 10 == 0 :
    factor = max_num//10
else:
    factor = math.ceil(max_num/10)

for fac in range(1, factor+1):
    print(check_num_for_factor(int_list, fac))


