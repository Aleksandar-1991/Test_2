arr01=input().split(',')
arr02=[]
for i in arr01:
    if i=='0':
        arr02.append(i)

for i in reversed(arr01):
    if int(i)<0:
        arr02.insert(0, i)

for i in arr01:
    if int(i)>0:
        arr02.append(i)

print(','.join(arr02))


