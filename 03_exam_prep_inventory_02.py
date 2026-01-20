shopping_list = input().split('!')

user_input = input()
while user_input != "Go Shopping!":
    command = user_input.split()
    action = command[0]
    if action == "Urgent":
        item = command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif action == "Unnecessary":
        item = command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in shopping_list:
            old_item_index = shopping_list.index(old_item)
            removed_item = shopping_list.pop(old_item_index)
            shopping_list.insert(old_item_index, new_item)
    elif action == "Rearrange":
        item = command[1]
        if item in shopping_list:
            item_index = shopping_list.index(item)
            shopping_list.append(shopping_list.pop(item_index))
    user_input = input()

print(", ".join(shopping_list))