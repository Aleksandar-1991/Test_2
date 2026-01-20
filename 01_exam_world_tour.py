destinations = input()

while (input_line := input()) != 'Travel':
    tokens = input_line.split(":")
    command = tokens[0]
    if command == "Add Stop":
        index, given_string = int(tokens[1]), tokens[2]
        if 0 <= index < len(destinations):
            destinations = destinations[:index] + given_string + destinations[index:]
    elif command == "Remove Stop":
        start_index, end_index = int(tokens[1]), int(tokens[2])
        if (0 <= start_index < len(destinations)) and (0 <= end_index < len(destinations)):
            substring = destinations[start_index:end_index+1]
            destinations = destinations.replace(substring, '')
    elif command == 'Switch':
        old_string, new_string = tokens[1], tokens[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
    print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")
