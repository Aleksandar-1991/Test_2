from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

gifts = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}


task01 = {"Doll", "Wooden train"}
task02 = {"Teddy bear", "Bicycle"}

crafted_toys = dict()

while materials and magic:
    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic[0] == 0:
        magic.popleft()
        continue

    magic_level = materials[-1] * magic[0]

    if magic_level in gifts.keys():
        toy = gifts[magic_level]
        if toy not in crafted_toys.keys():
            crafted_toys[toy] = 0
        crafted_toys[toy] += 1
        materials.pop()
        magic.popleft()
    elif magic_level < 0:
        materials.append(materials.pop() + magic.popleft())
    elif magic_level > 0:
        magic.popleft()
        materials[-1] += 15


if ("Doll" in crafted_toys.keys() and "Wooden train" in crafted_toys.keys()) or ("Teddy bear" in crafted_toys.keys() and "Bicycle" in crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}") if materials else None
print(f"Magic left: {', '.join(str(x) for x in magic)}") if magic else None
for key, value in sorted(crafted_toys.items()):
    print(f"{key}: {value}")
