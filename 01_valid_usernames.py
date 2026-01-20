all_usernames = input().split(", ")

def check_length(username: str) -> bool:
    if 3 <= len(username) <= 16:
        return True
    return False

def check_characters(username: str) -> bool:
    for char in username:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True

# def no_redundant_symbols(username: str) -> bool:
#     if " " in username:
#         return False
#     return True

def is_valid(username: str) -> bool:
    if (check_length(username) and check_characters(username)):
        return True
    return False

for username in all_usernames:
    if is_valid(username):
        print(username)