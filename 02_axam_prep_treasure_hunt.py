import copy

treasure_chest =  input().split("|")

command = input().split()

while command[0] != "Yohoho!":
    action = command[0]
    if action == "Loot":
        new_items = command[1:]
        for item in new_items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(command[1])
        if (index in range(len(treasure_chest))) or (index < 0 and index >= (-1)*len(treasure_chest)):
            dropped_item = treasure_chest.pop(index)
            treasure_chest.append(dropped_item)
    elif action == "Steal":
        stolen_items = int(command[1])
        if stolen_items > len(treasure_chest):
            print(", ".join(treasure_chest))
            treasure_chest.clear()
        else:
            removed_items = []
            for i in range(stolen_items):
                removed_items.insert(0, treasure_chest.pop(-1))
            print(", ".join(removed_items))
    command = input().split()
if len(treasure_chest) <= 0:
    print("Failed treasure hunt.")
else:
    treasure_chest_length = int()
    for item in treasure_chest:
        treasure_chest_length += len(item)
    average_gain = treasure_chest_length/len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
