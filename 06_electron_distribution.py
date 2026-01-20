electrons = int(input())
shell=1
lst_shells = []

while electrons>0:
    electrons_needed = 2 * (shell**2)
    if electrons>=electrons_needed:
        lst_shells.append(electrons_needed)
        electrons -= electrons_needed
        shell += 1
    else:
        lst_shells.append(electrons)
        electrons = 0


print (lst_shells)