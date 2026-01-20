all_cards=input().split()
shuffles=int(input())

deck_middle=len(all_cards)//2
deck01=[]
deck02=[]

for i in range(shuffles):
    deck01 = all_cards[:deck_middle]
    deck02 = all_cards[deck_middle:]
    all_cards.clear()
    for idx in range(len(deck01)):
        all_cards.append(deck01[idx])
        all_cards.append(deck02[idx])

print(all_cards)



