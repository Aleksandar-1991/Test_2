numbers = [int(x) for x in input().split()]
num = int(input())

def binary_search(numbers, num):
    left_index = 0
    right_index = len(numbers) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_el = numbers[mid_index]

        if mid_el == num:
            return mid_index
        elif mid_el < num:
            left_index = mid_index + 1
        else:
            right_index = mid_index -1

    return -1
print(binary_search(numbers, num))
