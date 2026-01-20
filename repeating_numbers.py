lines=int(input())
arr01=[]

for i in range(lines):
    arr01.append(int(input()))

count=int()
max_count=int()
max_value=int()
sec_max_cnt=int()
sec_max_val=int()
values_used=[]

for i in range(len(arr01)):
    if arr01[i] not in values_used:
        if arr01.count(arr01[i])>max_count:
            sec_max_cnt=max_count
            sec_max_val=max_value
            max_count=arr01.count(arr01[i])
            max_value=arr01[i]
            values_used.append(arr01[i])
        elif arr01.count(arr01[i])>sec_max_cnt:
            sec_max_cnt=arr01.count(arr01[i])
            sec_max_val=arr01[i]
            values_used.append(arr01[i])
        else:
            values_used.append((arr01[i]))

if max_count==sec_max_cnt and max_value<sec_max_val:
    print(max_value)
elif max_count==sec_max_cnt and max_value>sec_max_val:
    print(sec_max_val)
else:
    print(max_value)

print(values_used)


# print(max_count)
# print(max_value)
# print(sec_max_cnt)
# print(sec_max_val)





