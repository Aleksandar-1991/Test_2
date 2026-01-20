snowball=int(input())



highest_value=str()
max_value=int()

for ball in range(snowball):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value>max_value:
        max_value=snowball_value
        highest_value=f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"

print(highest_value)
