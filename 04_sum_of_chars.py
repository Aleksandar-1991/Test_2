lines=int(input())
total_sum=0

for line in range(lines):
    char=input()
    total_sum+= ord(char)

print(f"The sum equals: {total_sum}")