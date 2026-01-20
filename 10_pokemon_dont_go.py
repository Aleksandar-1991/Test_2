distances = list(map(int, input().split()))
sum_removed_elements = int()

def adjust_list(my_list: list, removed: int) -> list:
    for element in range(len(my_list)):
        if my_list[element] <= removed:
            my_list[element] += removed
        elif my_list[element] > removed:
            my_list[element] -= removed
    return my_list

while len(distances)>0:
    index = int(input())
    removed_element = int()
    if index<0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[-1])
        distances = adjust_list(distances, removed_element)
        sum_removed_elements += removed_element
    elif index>=len(distances):
        removed_element = distances.pop(-1)
        distances.append(distances[0])
        distances = adjust_list(distances, removed_element)
        sum_removed_elements += removed_element
    else:
        removed_element = distances[index]
        distances = adjust_list(distances, distances.pop(index))
        sum_removed_elements += removed_element


print(sum_removed_elements)

