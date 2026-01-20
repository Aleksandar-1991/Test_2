n = int(input())

regular = set()
vip = set()

for i in range(n):
    reservation = input()
    first_char = reservation[0]
    if first_char.isdigit():
        vip.add(reservation)
    else:
        regular.add(reservation)


while (res_number := input()) != 'END':
    if res_number in vip:
        vip.remove(res_number)
    elif res_number in regular:
        regular.remove(res_number)

total_guests = len(regular) + len(vip)

sorted_vip = sorted(list(vip))
sorted_regular = sorted(list(regular))
print(total_guests, *sorted_vip, *sorted_regular, sep='\n')



