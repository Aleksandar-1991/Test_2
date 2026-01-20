def smallest_number(given_list: list) -> int:
    list_min=min(given_list)
    return list_min

my_list=[]
for num in range(3):
    my_list.append(int(input()))
print(smallest_number(my_list))