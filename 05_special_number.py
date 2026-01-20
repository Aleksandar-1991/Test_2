number=int(input())

for i in range(1,number+1):
    temp=str(i)
    sum=0
    for dig in temp:
        sum+=int(dig)
    if sum==5 or sum==7 or sum==11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
