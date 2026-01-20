from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted_water = 0
filled_cups = list()

while cups and bottles:
    current_bottle = bottles.pop()
    if current_bottle >= cups[0]:
        wasted_water += (current_bottle - cups[0])
        filled_cups.append(cups.popleft())
    else:
        cups[0] -= current_bottle
        # wasted_water += current_bottle

if not cups:
    print(f"Bottles:", *(reversed(bottles)))
elif not bottles:
    print(f"Cups:", *(cups))

print(f"Wasted litters of water: {wasted_water}")

