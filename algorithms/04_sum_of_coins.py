coins = sorted([int(el) for el in input().split(", ")])
total_amount = int(input())

def calculate_coins(coins_list, total_amount):
    coins_dict = {}
    num_coins = 0

    for coin in coins_list:
        coins_dict[coin] = []

    for coin in sorted(coins_dict.keys(), reverse=True):
        if total_amount // coin > 0:
            c_number = total_amount // coin
            coins_dict[coin] = c_number
            total_amount %= coin
            num_coins += c_number


    if total_amount:
        print("Error")
        exit()

    result = f"Number of coins to take: {num_coins}\n"
    for key, value in sorted(coins_dict.items(), reverse=True):
        if value:
            result += f"{value} coin(s) with value {key}\n"

    return result

print(calculate_coins(coins, total_amount))



