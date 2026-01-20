list01 = input().split(", ")

def palindrome_check(list02: list) -> bool:
    for i in list02:
        if i==i[::-1]:
            print("True")
        else:
            print("False")

palindrome_check(list01)


