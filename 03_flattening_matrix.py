n = int(input())

nums = list()
for i in range(n):
    row_data = [int(el) for el in input().split(", ")]
    nums.extend(row_data)
print(nums)