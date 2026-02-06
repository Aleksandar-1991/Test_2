def bubble_sort(numbers):
    is_sorted = False
    sorted_numbers = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(numbers) - sorted_numbers):
            i = j - 1
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                is_sorted = False
        sorted_numbers += 1

numbers = [int(x) for x in input().split()]

bubble_sort(numbers)

print(*numbers)
