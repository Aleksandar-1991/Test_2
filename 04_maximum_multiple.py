divisor=int(input())
boundary=int(input())
largest_n=int()

for i in range(boundary,divisor, -1):
    if i % divisor == 0:
        largest_n=i
        print(largest_n)
        break
