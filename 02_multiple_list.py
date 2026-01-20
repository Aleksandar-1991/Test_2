factor=int(input())
count=int(input())

list01=[]

for i in range(factor, (factor * count)+1):
    if i%factor==0:
        list01.append(i)

print(list01)

