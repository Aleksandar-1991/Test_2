given_string = input()
result = str()

for char in given_string:
    new_char = ord(char) + 3
    result += chr(new_char)

print(result)