from operator import index

some_tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']

def uninterrupted_number_of_symbols(word: str, char: str) -> int:
    max_num = 0
    last_character = str()
    counter = 0
    for index in range(len(word)):
        if word[index] == char:
            if word[index] == last_character:
                counter += 1
            else:
                last_character = word[index]
                counter += 1
        else:
            if max_num < counter:
                max_num = counter
            counter = 0
            last_character = word[index]
    if max_num < counter:
        max_num = counter
    return max_num


for ticket in some_tickets:
    ticket = ticket.strip()
    valid_ticket = False
    winning_ticket = False
    jackpot_ticket = False
    uninterrupted_match_length = 0
    symbol = str()
    if len(ticket) == 20:
        valid_ticket = True
    for sym in winning_symbols:
        temp_value = min(uninterrupted_number_of_symbols(ticket[:10], sym), uninterrupted_number_of_symbols(ticket[10:], sym))
        if temp_value >= 6:
            winning_ticket = True
            uninterrupted_match_length = temp_value
            symbol = sym
        if (sym * 20) in ticket:
            jackpot_ticket = True
            symbol = sym
    if jackpot_ticket:
        print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
    elif winning_ticket:
        print(f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}')
    elif valid_ticket:
        print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")






