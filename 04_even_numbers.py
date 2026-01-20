n=int(input())
all_even=True

for i in range(n):
    num=int(input())
    if num % 2 == 1:
        print(f"{num} is odd!")
        all_even=False
        break

if all_even==True:
    print("All numbers are even.")

