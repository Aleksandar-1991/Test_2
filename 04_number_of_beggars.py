sums=input().split(", ")
beggers=int(input())

iteration_start=0
collected_items=[]


for beggar in range(beggers):
    temp_sum = 0
    for i in range(beggar, len(sums), beggers):
        temp_sum += int(sums[i])
    iteration_start += 1
    collected_items.append(temp_sum)

print(collected_items)