word = input()
result = ''

explosions = 0
for index in range(len(word)):
    if word[index] == '>':
        explosions += int(word[index+1])
        result += word[index]
    else:
        if explosions:
            explosions -= 1
        else:
            result += word[index]

print(result)


