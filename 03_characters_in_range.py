def char_in_range(ch01: str, ch02: str) -> list:
    start_chr = ord(ch01) + 1
    finish_chr = ord(ch02)
    my_list = []

    for i in range(start_chr,finish_chr):
        my_list.append(chr(i))
    return my_list

a = input()
b = input()


print((" ").join(char_in_range(a,b)))