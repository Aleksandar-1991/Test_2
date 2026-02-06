def selection_sort(numbers):
    for idx in range(len(numbers)):
        min_idx = idx
        for current_index in range(idx + 1, len(numbers)):
            if numbers[current_index] < numbers[min_idx]:
                min_idx = current_index
        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

input_numbers = list(map(int, input().split()))

selection_sort(input_numbers)
print(*input_numbers)