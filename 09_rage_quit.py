word = input()
unique_symbols = str()

result = str()
temp_string = str()
multiplier = ''
last_character = str()
for char in word:
    if not char.isdigit() and last_character.isdigit():
        result += int(multiplier) * temp_string
        temp_string = ''
        multiplier = ''
        temp_string += char.upper()
    elif not char.isdigit() and not last_character.isdigit():
        temp_string += char.upper()
    elif char.isdigit():
        multiplier += char
    last_character = char
result += int(multiplier) * temp_string

for char in result:
    if char not in unique_symbols:
        unique_symbols += char

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)
