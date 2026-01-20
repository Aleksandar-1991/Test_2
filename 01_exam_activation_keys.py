raw_key = input()

while (input_line := input()) != 'Generate':
    tokens = input_line.split(">>>")
    command = tokens[0]
    if command == 'Contains':
        substring = tokens[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif command == 'Flip':
        upper_lower, start_index, end_index = tokens[1], int(tokens[2]), int(tokens[3])
        substring = raw_key[start_index: end_index]
        if upper_lower == "Upper":
            new_string = substring.upper()
            raw_key = raw_key.replace(raw_key[start_index: end_index], new_string)
        elif upper_lower == 'Lower':
            new_string = substring.lower()
            raw_key = raw_key.replace(raw_key[start_index: end_index], new_string)
        print(raw_key)

    elif command == 'Slice':
        start_index, end_index = int(tokens[1]), int(tokens[2])
        substring = raw_key[start_index: end_index]
        raw_key = raw_key.replace(raw_key[start_index: end_index], "")
        print(raw_key)

print(f'Your activation key is: {raw_key}')