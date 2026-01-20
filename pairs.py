predef_sum=int(input())
arr01=[int(el) for el in input().split()]
arr02=[]
result=''

for i in range(len(arr01)):
        arr02=arr01[i+1:len(arr01)]
        for j in arr02:
            if arr01[i]+j==predef_sum:
                result+=f"\n{arr01[i]},{j}"

if result=='':
    print("no pairs")
else:
    print(result)

