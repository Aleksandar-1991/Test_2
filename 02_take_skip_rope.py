initial_list = input()
numbers_list = []
non_numbers_list = []
result_string = []

for idx in range(len(initial_list)):
    if initial_list[idx].isdigit():
        numbers_list.append(int(initial_list[idx]))
    else:
        non_numbers_list.append(initial_list[idx])

take_list = []
skip_list = []

for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

for j in range(len(take_list)):
    result_string.extend(non_numbers_list[:take_list[j]])
    non_numbers_list = non_numbers_list[take_list[j]:]
    non_numbers_list = non_numbers_list[skip_list[j]:]

print("".join(result_string))





