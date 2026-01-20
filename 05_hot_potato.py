from collections import deque

names = deque(input().split())
n = int(input())

while len(names) != 1:
    names.rotate(-(n-1))
    removed = names.popleft()
    print(f"Removed {removed}")

print(f"Last is {names[0]}")