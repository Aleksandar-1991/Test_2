lines=int(input())

capacity=255
free_space=capacity

for line in range(lines):
    amount_to_pour=int(input())
    if amount_to_pour>free_space:
        print("Insufficient capacity!")
        continue
    else:
        free_space -= amount_to_pour

print(255-free_space)
