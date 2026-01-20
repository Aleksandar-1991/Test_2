word = input()
counter = dict()

for char in word:
    if char != " ":
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    else:
        continue

for (key, value) in counter.items():
    print(f"{key} -> {value}")