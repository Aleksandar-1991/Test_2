team_a = [f"A-{number}" for number in range(1, 12)]
team_b = [f"B-{number}" for number in range(1, 12)]

cards = input().split()
game_terminated=False


for card in cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    else:
        continue
    if len(team_a)<7 or len(team_b)<7:
        game_terminated=True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_terminated==True:
    print("Game was terminated")