text = input()

parentheses = {
    '(':')',
    '{':'}',
    '[':']'
}

temp_stack = list()

for char in text:
    if char in parentheses.keys():
        temp_stack.append(char)
    elif char in parentheses.values():
        if not temp_stack:
            print('NO')
            break
        last_char = temp_stack.pop()
        if parentheses[last_char] != char:
            print('NO')
            break
else:
    if temp_stack:
        print('NO')
    else:
        print('YES')