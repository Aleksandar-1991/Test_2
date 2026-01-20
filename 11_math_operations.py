from collections import deque

def math_operations(*args, **kwargs):
    # print(kwargs.items())
    key_words_list = deque()
    for key, value in kwargs.items():
        key_words_list.append([key, value])
    kwargs = key_words_list

    mapper = {
        "a": lambda x, y: x + y,
        "s": lambda x, y: x - y,
        "d": lambda x, y: x / y if y != 0 else None,
        "m": lambda x, y: x * y
    }

    for num in args:
        new_value = mapper[kwargs[0][0]](kwargs[0][1], num)
        if new_value != None:
            kwargs[0][1] = new_value

        kwargs.rotate(-1)
    sorted_values = sorted(key_words_list, key= lambda kvp: (-kvp[1], kvp[0]))
    result = ''
    for key,value in sorted_values:
        result += f"{key}: {value:.1f}\n"
    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))




