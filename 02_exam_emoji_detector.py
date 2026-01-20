import re
cool_treshold = 1
expression = r'((\:{2}|\*{2})([A-Z][a-z]{2,})\2)'
emoji_dictionary = dict()
line = input()

for char in line:
    if char.isdigit():
        cool_treshold *= int(char)

emojis = re.findall(expression, line)
number_of_emojis = len(emojis)
for em in emojis:
    full_emoji, word_only = em[0], em[2]
    emoji_coolness = 0
    for ch in word_only:
        emoji_coolness += ord(ch)
    emoji_dictionary[full_emoji] = emoji_coolness

print(f"Cool threshold: {cool_treshold}")
print(f"{len(emoji_dictionary.keys())} emojis found in the text. The cool ones are:")
for item in emoji_dictionary.keys():
    if emoji_dictionary[item] >= cool_treshold:
        print(item)

