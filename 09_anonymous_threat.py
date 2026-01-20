import copy

initial_list = input().split()
final_list = []

while True:
    user_input = input()
    if user_input == "3:1":
        break
    else:
        command = user_input.split()
        action = command[0]
        if action == "merge":
            start_index = int(command[1])
            if start_index > len(initial_list)-1:
                continue
            # elif start_index < 0 and start_index >= (-1)*len(initial_list):
            #     start_index += len(initial_list)
            #print(start_index)
            end_index = int(command[2])
            if end_index >= len(initial_list):
                end_index = len(initial_list)-1
            elif end_index < 0:
                end_index += len(initial_list)
            #print(end_index)
            temp_list = []
            temp_word = str()

            for idx in range(len(initial_list)):
                if len(temp_list) == 0:
                    temp_list.append(initial_list[idx])
                elif start_index + 1 <= idx and idx <= end_index:
                        temp_list[-1] = temp_list[-1] + initial_list[idx]
                elif start_index + 1 > idx or idx > end_index:
                        temp_list.append(initial_list[idx])

            initial_list = copy.deepcopy(temp_list)
            temp_list.clear()

        elif action == "divide":
            index = int(command[1])
            # if index >= 0:
            #     pass
            if index < 0 and index >= (-1)*len(initial_list):
                index += len(initial_list)
            # else:
            #     continue
            partitions = int(command[2])
            if partitions == 0:
                continue
            temp_list_divide = []
            temp_word_divide = str()
            for idx in range(len(initial_list)):
                if idx != index:
                    temp_list_divide.append(initial_list[idx])
                else:
                    temp_word_divide = initial_list[idx]
                    letter_in_division = len(initial_list[index])//partitions
                    division_counter=0
                    for i in range(0,len(temp_word_divide)-1, letter_in_division):
                        if division_counter != partitions - 1:
                            current_word_part = temp_word_divide[i:i + letter_in_division]
                            temp_list_divide.append(current_word_part)
                            division_counter += 1
                        elif division_counter == partitions - 1:
                            current_word_part = temp_word_divide[i:]
                            temp_list_divide.append(current_word_part)
                            division_counter += 1
            initial_list = copy.deepcopy(temp_list_divide)


print(" ".join(initial_list))


