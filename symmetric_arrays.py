lines=int(input())

for i in range(lines):
    arr01=input().split()
    result=''
    for j in range(len(arr01)):
        if arr01[j]==arr01[len(arr01)-1-j]:
            result='Yes'
            continue
        elif arr01[j]!=arr01[len(arr01)-1-j]:
            result='No'
    print(result)
