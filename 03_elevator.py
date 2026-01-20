people=int(input())
elevator_capacity=int(input())

if people%elevator_capacity>0:
    print(people//elevator_capacity + 1)
else:
    print(people//elevator_capacity)