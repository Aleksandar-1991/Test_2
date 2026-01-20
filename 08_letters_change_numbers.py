some_string = input().split()
total_sum = 0

for word in some_string:
    number = int(word[1:-1])
    result = float()
    if word[0].isupper():
        result = number / (ord(word[0]) - 64)
    else:
        result = number * (ord(word[0]) - 96)

    if word[-1].isupper():
        result -= (ord(word[-1]) - 64)
    else:
        result += (ord(word[-1]) - 96)
    total_sum += result
print(f"{total_sum:.2f}")
