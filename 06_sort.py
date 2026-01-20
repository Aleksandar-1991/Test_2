my_list = list(map(int, input().split()))

def sort_ascending(list01: list) -> list:
    new_list = sorted(list01)
    return new_list

print(sort_ascending(my_list))