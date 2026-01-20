text = input()

digits_found = str()
letters_found = str()
other_found = str()

for ch in text:
    if ch.isdigit():
        digits_found += ch
    elif ch.isalpha():
        letters_found += ch
    else:
        other_found += ch

print(f"{digits_found}\n{letters_found}\n{other_found}")