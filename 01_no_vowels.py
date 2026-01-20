word = input()
forbidden_letters = ['a', 'o', 'u', 'e', 'i']

new_word = [letter for letter in word if letter.lower() not in forbidden_letters]

new_word=''.join(new_word)
print(new_word)