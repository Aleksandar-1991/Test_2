import re
text = input()

expression = r'(\#|\@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

words = re.findall(expression, text)
matches = list()


for match in words:
    first_word, second_word = match[1], match[2]
    if first_word [::-1] == second_word:
        matches.append(first_word)
        matches.append(second_word)


if words:
    valid_pairs = len(words)
    print(f"{valid_pairs} word pairs found!")
else:
    print("No word pairs found!")
if matches:
    print(f"The mirror words are:")
    result = list()
    for idx in range(0, len(matches), 2):
        result.append(f"{matches[idx]} <=> {matches[idx+1]}")
    print(", ".join(result))
else:
    print("No mirror words!")
