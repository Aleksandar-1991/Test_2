my_list = list(map(int, input().split(".")))

my_list[-1] += 1

for idx in range(len(my_list)-1, 0, -1):
    if my_list[idx]>9:
        my_list[idx]=0
        my_list[idx-1] += 1

new_list = [str(digit) for digit in my_list]
print('.'.join(new_list))
