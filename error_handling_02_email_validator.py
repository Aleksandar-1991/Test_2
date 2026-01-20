from importlib.metadata import pass_none


class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

valid_domains = (".com", ".bg", ".net", ".org")
MIN_LEN_EMAIL = 4

while (command := input()) != "End":
    at_index = command.index("@")
    email_first_part = command[:at_index]
    email_second_part = command[at_index:]


    if len(email_first_part) <= MIN_LEN_EMAIL:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    if not email_second_part.endswith(valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")





