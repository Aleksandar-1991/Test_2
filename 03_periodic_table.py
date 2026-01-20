n = int(input())
elements = set()

for i in range(n):
    data = input().split()
    for el in data:
        if el not in elements:
            elements.add(el)

print(*elements, sep='\n')