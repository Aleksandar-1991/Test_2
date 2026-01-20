n, m = list(map(int, input().split()))

set_n = {input() for i in range(n)}
set_m = {input() for i in range(m)}



# for num in range(n+m):
#     if len(set_n) < n:
#         set_n.add(input())
#     else:
#         set_m.add(input())

set_diff = set_n.intersection(set_m)
print(*set_diff, sep='\n')

