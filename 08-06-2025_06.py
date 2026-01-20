location=int(input())



for i in range(location):
    gold_yield = float()
    daily_expected_yield=float(input())
    days_in_mine=int(input())
    for j in range(days_in_mine):
        daily_yield=int(input())
        gold_yield+=daily_yield
    if daily_expected_yield<=(gold_yield / days_in_mine):
        print(f"Good job! Average gold per day: {(gold_yield / days_in_mine):.2f}.")
    else:
        gold_needed=daily_expected_yield - (gold_yield / days_in_mine)
        print(f"You need {gold_needed:.2f} gold.")
