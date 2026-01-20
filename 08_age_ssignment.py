def age_assignment(*args, **kwargs):
    names = dict()
    for name in args:
        for key, value in kwargs.items():
            if name.startswith(key):
                names[name] = value
    sorted_names = sorted(names.items(), key= lambda kvp: kvp[0])
    result = ""
    for key, value in dict(sorted_names).items():
        result += f"{key} is {value} years old.\n"
    return result




print(age_assignment("Peter", "George", "Pamela", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))