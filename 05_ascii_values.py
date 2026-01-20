characters = input().split(", ")

my_dict = {char: ord(char) for char in characters}

print(my_dict)