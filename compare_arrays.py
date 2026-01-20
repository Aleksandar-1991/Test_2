arrlen=int(input())
arr01=[]
arr02=[]
result=''
for i in range(arrlen):
    arr01.append(int(input()))
for j in range(arrlen):
    arr02.append(int(input()))

for i in range(arrlen):
    if arr01[i]!=arr02[i]:
        result='not equal'
    else:
        result='equal'

print(result)

