def sum_numbers(num01: int, num02: int) -> int:
    a = num01 + num02
    return a

def subtract(num_sum: int, num03: int) -> int:
    b = num_sum - num03
    return b

def add_and_subtract(num_list: list) -> int:
    res=sum_numbers(my_list[0], my_list[1])
    final_res=subtract(res, my_list[2])
    return final_res

my_list=[]
for i in range(3):
    my_list.append(int(input()))

print(add_and_subtract(my_list))

