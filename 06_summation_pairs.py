import time

numbers = list(map(int, input().split()))
target = int(input())

start = time.time()
targets = set()
values_map = dict()
for num in numbers:
    if num in targets:
        targets.remove(num)
        pair = values_map[num]
        del values_map[num]
        print(f"{pair} + {num} = {target}")
    else:
        num_needed = target - num
        targets.add(num_needed)
        values_map[num_needed] = num
end = time.time()
print(end-start)



