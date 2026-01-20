lines=int(input())

for i in range(lines):
    arr01=input().split(',')
    prev_el=int()
    result = None
    for j in range(len(arr01)):
        if int(arr01[j])<prev_el:
            result=False
            break
        elif int(arr01[j])>prev_el:
            result=True
            prev_el=int(arr01[j])

    print(result)


