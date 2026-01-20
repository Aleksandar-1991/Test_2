items = {'shards': 0, 'fragments': 0, 'motes': 0}
item_found = False

def check_key_items(dict_items: dict) -> bool:
    if dict_items['shards'] >= 250:
        dict_items['shards'] -= 250
        print("Shadowmourne obtained!")
        return True
    elif dict_items['fragments'] >= 250:
        print(items['fragments'])
        dict_items['fragments'] -= 250
        print(items['fragments'])
        print("Valanyr obtained!")
        return True
    elif dict_items['motes'] >= 250:
        dict_items['motes'] -= 250
        print("Dragonwrath obtained!")
        return True
    else:
        return False

while True:
    line_of_items = input().split()
    number_of_items_in_a_line = int(len(line_of_items))
    for index in range(1, number_of_items_in_a_line, 2):
        new_item = line_of_items[index].lower()
        quantity = int(line_of_items[index -1])
        if new_item not in items.keys():
            items[new_item] = 0
        items[new_item] += quantity
        if check_key_items(items):
            item_found = True
            break
    if item_found:
        break


# for (key, value) in items.items():
#     print(f"{key}: {value}")


