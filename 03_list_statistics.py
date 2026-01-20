n=int(input())

positive=[]
negative=[]
count_positive=int()
sum_negative=int()

for x in range(n):
    num=int(input())
    if num>=0:
        count_positive += 1
        positive.append(num)
    else:
        sum_negative += num
        negative.append(num)

print(positive)
print(negative)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")