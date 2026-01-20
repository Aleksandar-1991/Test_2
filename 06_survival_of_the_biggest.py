new_list=input().split()
count=int(input())


while count>0:
    min = 1000000
    for num in new_list:
        if int(num)<min:
            min=int(num)
    new_list.remove(str(min))
    count -= 1

final_list=(", ".join(new_list))

print(final_list)

