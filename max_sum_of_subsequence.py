line=int(input())
arr01=[]
temp_sum=int()
maximal_sum=int()

for i in range(line):
    arr01.append(int(input()))
    temp_sum+=arr01[i]
    if temp_sum<0:
        temp_sum=0
    if temp_sum>maximal_sum:
        maximal_sum=temp_sum

print(maximal_sum)


