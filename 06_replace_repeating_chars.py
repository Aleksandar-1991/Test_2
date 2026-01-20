text = input()
result = str()
last_char = ""
for index in range(len(text)):
    if text[index] == last_char:
        continue
    else:
        last_char = text[index]
        result += last_char

print(result)


