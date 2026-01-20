clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks = 0

while clothes:
    racks += 1
    temp_rack = rack_capacity
    while clothes and clothes[-1] <= temp_rack:
        temp_rack -= clothes.pop()

print(racks)