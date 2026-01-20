my_list = input().split()
palindrome = input()

palindrome_list = [word for word in my_list if word==word[::-1]]
palindrome_count = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")


