arr01=input().split()
for i in range(len(arr01)):
    arr01[i]=int(arr01[i])

result=''
if arr01[0]>arr01[1]:
    for i in range(1, len(arr01), 1):
        if i%2==1 and arr01[i-1]>arr01[i]:
            result='yes'
        elif i%2==0 and arr01[i-1]<arr01[i]:
            result='yes'
        else:
            result='no'
            break
if arr01[0]<arr01[1]:
    for i in range(1, len(arr01), 1):
        if i%2==1 and arr01[i-1]<arr01[i]:
            result='yes'
        elif i%2==0 and arr01[i-1]>arr01[i]:
            result='yes'
        else:
            result='no'
            break

print(result)



