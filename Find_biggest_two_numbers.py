arr01=input().split()

max_num=int()
second_max_num=int()

for i in range(len(arr01)):
    if int(arr01[i])>max_num:
        second_max_num=max_num
        max_num=int(arr01[i])
    elif int(arr01[i])>second_max_num:
        second_max_num=int(arr01[i])

print(max_num)
print(second_max_num)



