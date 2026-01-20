my_to_do_list = []

while True:
    task = input()
    if task == "End":
        break
    else:
        my_to_do_list.append(task)

    sorted_notes = sorted(my_to_do_list, key=lambda x: int(x.split('-')[0]))
    result = [note.split("-")[1] for note in sorted_notes ]

print(result)

