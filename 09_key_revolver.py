from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

shots = 0

while bullets and locks:
    shots += 1
    intelligence_value -= bullet_price
    current_bullet = bullets.pop()
    if locks[0] >= current_bullet:
        locks.popleft()
        print(f"Bang!")
    else:
        print("Ping!")

    if shots == gun_barrel and bullets:
        shots = 0
        print("Reloading!")

if not locks:
    bullets_left = len(bullets)
    print(f"{bullets_left} bullets left. Earned ${intelligence_value}")
else:
    locks_left = len(locks)
    print(f"Couldn't get through. Locks left: {locks_left}")


