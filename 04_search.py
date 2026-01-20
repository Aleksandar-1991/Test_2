n=int(input())
word=input()

full_list=[]
sorted_list=[]
for num in range(n):
    full_list.append(input())
    if word in full_list[num]:
        sorted_list.append(full_list[num])

print(full_list)
print(sorted_list)