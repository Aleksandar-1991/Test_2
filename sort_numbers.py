arr01=input().split(', ')

for i in range(len(arr01)):
    arr01[i]=int(arr01[i])

arr01.sort(reverse=True)

for i in range(len(arr01)):
    arr01[i]=str(arr01[i])

print(', '.join(arr01))