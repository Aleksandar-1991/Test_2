user_pass = input()


def check_string_length(string01: str) -> int:
    return len(string01)

def is_only_letters_and_digits(string02: str) -> bool:
    return string02.isalnum()

def number_of_digits(string03: str) -> int:
    counter_of_digits=0
    for i in string03:
        if i.isdigit():
            counter_of_digits += 1
    return counter_of_digits


def check_password_complexity(password: str) -> str:
    error_message_list=[]
    if check_string_length(password)<6 or check_string_length(password)>10:
        error_message_list.append("Password must be between 6 and 10 characters")
    if not is_only_letters_and_digits(password):
        error_message_list.append("Password must consist only of letters and digits")
    if number_of_digits(password)<2:
        error_message_list.append("Password must have at least 2 digits")

    if len(error_message_list)>0:
        print(("\n".join(error_message_list)))
    else:
        print("Password is valid")

check_password_complexity(user_pass)





