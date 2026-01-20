class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

MIN_LEN_EMAIL = 4
valid_domains = (".com", ".bg", ".org", ".net")

while (user_input := input()) != "End":
    if len(user_input.split("@")[0]) <= MIN_LEN_EMAIL:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in user_input:
        raise MustContainAtSymbolError("Email must contain @")
    if not user_input.endswith(valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")

