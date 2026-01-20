arr01=input().split(',')
avg=float()
below=[]
above=[]
sum=float()

for i in range(len(arr01)):
    arr01[i]=int(arr01[i])
    sum+=arr01[i]

avg=sum/len(arr01)

for i in range(len(arr01)):
    if arr01[i]<avg:
        below.append(str(arr01[i]))
    elif arr01[i]>avg:
        above.append(str(arr01[i]))

print(f"{avg:.2f}")
print(",".join(below))
print(','.join(above))










