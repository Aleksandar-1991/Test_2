n = int(input())

odd_results = set()
even_results = set()

for i in range(1, n + 1):
    name = input()
    total = int()
    for j in name:
        total += ord(j)
    total = total//i
    if total % 2 == 0:
        even_results.add(total)
    else:
        odd_results.add(total)


sum_odd = sum(odd_results)
sum_even = sum(even_results)

if sum_even == sum_odd:
    union_results = odd_results.union(even_results)
    print(*union_results, sep=', ')
elif sum_odd > sum_even:
    sum_diff = odd_results.difference(even_results)
    print(*sum_diff, sep=', ')
elif sum_even > sum_odd:
    sum_symm_diff = even_results.symmetric_difference(odd_results)
    print(*sum_symm_diff, sep=', ')

