num=int(input())
row1=''

for i in range(num):
    row1+='*'
    print(row1)

for j in range((num-1), -1, -1):
    row1=row1[:-1]
    print(row1)



