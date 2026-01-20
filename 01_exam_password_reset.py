given_string = input()

while (input_line := input()) != 'Done':
    tokens = input_line.split()
    if input_line == 'TakeOdd':
        temp_string = given_string
        given_string = ''
        for idx in range(1, len(temp_string),2):
            given_string += temp_string[idx]
        print(given_string)
    else:
        command = tokens[0]
        if command == 'Cut':
            index, length = int(tokens[1]), int(tokens[2])
            substring = given_string[index: index+length]
            given_string = given_string.replace(substring, '', 1)
            print(given_string)
        elif command == 'Substitute':
            substring, substitute = tokens[1], tokens[2]
            if substring in given_string:
                given_string = given_string.replace(substring, substitute)
                print(given_string)
            else:
                print("Nothing to replace!")

print(f"Your password is: {given_string}")