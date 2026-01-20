username = input()

while (line := input()) != "Registration":
    tokens = line.split()
    command = tokens[0]
    if command == "Letters":
        case = tokens[1]
        if case == 'Lower':
            username = username.lower()
            print(username)
        else:
            username = username.upper()
            print(username)
    elif command == 'Reverse':
        startindex = int(tokens[1])
        endindex = int(tokens[2])+1
        if (0 <= startindex < len(username)) and (0 <= endindex < len(username)):
            temp_string = username[startindex:endindex]
            reversed_str = temp_string[::-1]
            print(reversed_str)
    elif command == 'Substring':
        substring = tokens[1]
        if substring in username:
            new_username = username.replace(substring, "", 1)
            print(new_username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif command == 'Replace':
        new_char = tokens[1]
        username = username.replace(new_char, "-")
        print(username)
    elif command == 'IsValid':
        is_valid_char = tokens[1]
        if is_valid_char in username:
            print("Valid username.")
        else:
            print(f"{is_valid_char} must be contained in your username.")


