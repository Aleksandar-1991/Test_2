def even_odd_filter(**kwargs):
    for name, nums in kwargs.items():
        if name == "even":
            kwargs[name] = [el for el in nums if el % 2 == 0]
        else:
            kwargs[name] = [el for el in nums if el % 2 != 0]
    return dict(sorted(kwargs.items(), key= lambda kvp: -len(kvp[1])))




print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

