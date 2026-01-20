given_words = input().split()
new_words = []
for word in given_words:
    digits_in_word = ''
    letters_in_word = ''
    word = [str(char) for char in word]
    for idx in range(len(word)):
        if word[idx].isdigit():
            digits_in_word += word[idx]
        else:
            letters_in_word = word[idx:]
            break
    letters_in_word[0], letters_in_word[-1] = letters_in_word[-1], letters_in_word[0]
    new_word = chr(int(digits_in_word)) + "".join(letters_in_word)
    new_words.append(new_word)

print(" ".join(new_words))


