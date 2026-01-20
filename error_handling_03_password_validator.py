class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError(Exception):
    pass
class PasswordNoSpecialCharactersError(Exception):
    pass
class PasswordContainsSpacesError(Exception):
    pass

SPECIAL_CHARACTERS = ("@", "*", "&", "%")
PASSWORD_MINIMUM_LENGTH = 8

def common_password(pwd, special_chars):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_special_chars = all(ch in special_chars for ch in pwd)
    return any([only_digits, only_letters, only_special_chars])

while (password := input()) != "Done":
    contains_special_characters = any( ch in SPECIAL_CHARACTERS for ch in password)
    if len(password) < PASSWORD_MINIMUM_LENGTH  :
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if common_password(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    if not contains_special_characters:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
