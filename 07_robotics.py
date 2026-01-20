from collections import deque

temp_robots = deque(input().split(";"))
robots = dict()
available_robots = deque()

while temp_robots:
    rob_data = (temp_robots.popleft()).split("-")
    rob_name, proc_time = rob_data[0], int(rob_data[1])
    robots[rob_name] = {'process_time': proc_time, 'processing_until': 0}



start_time = list(map(int, input().split(":")))
hours, minutes, seconds = start_time[0], start_time[1], start_time[2]
current_seconds = (((hours * 60) + minutes) * 60) + seconds
products = deque()

while (product := input()) != 'End':
    products.append(product)


def sec_to_full_time(given_seconds: int) -> str:
    seconds = given_seconds % 60
    minutes = (given_seconds // 60) % 60
    hours = given_seconds // 3600
    if hours >= 24:
        hours %= 24
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

while products:
    current_seconds += 1
    for name in robots.keys():
        if name not in available_robots and current_seconds >= robots[name]['processing_until']:
            robots[name]['processing_until'] = 0
            available_robots.append(name)
    current_product = products.popleft()
    if available_robots:
        robot = available_robots.popleft()
        robots[robot]['processing_until'] = current_seconds + robots[robot]['process_time']
        current_time = sec_to_full_time(current_seconds)
        print(f"{robot} - {current_product} [{current_time}]")
    else:
        products.append(current_product)
