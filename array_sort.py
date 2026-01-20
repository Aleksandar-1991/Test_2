arr01=input().split(',')
arr02=arr01.copy()

for i in range(len(arr01)):
    if arr01[i]=='0':
        arr02.append(arr01[i])
        arr02.remove(arr01[i])

print(','.join(arr02))


