text = input()
letters = dict()

for char in text:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

sorted_letters = sorted(letters.items())

for key, value in sorted_letters:
    print(f"{key}: {value} time/s")