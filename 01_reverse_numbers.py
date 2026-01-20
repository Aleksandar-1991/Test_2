from collections import deque

nums = input().split()

reversed_stack = deque()

while nums:
    reversed_stack.append(nums.pop())

print(" ".join(reversed_stack))
