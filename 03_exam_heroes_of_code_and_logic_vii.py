n = int(input())
heroes = dict()

for i in range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {'hp': int(hp), 'mp': int(mp)}

while (input_line := input()) != 'End':
    tokens = input_line.split(" - ")
    command = tokens[0]
    if command == 'CastSpell':
        hero, mp_needed, spell_name = tokens[1], int(tokens[2]), tokens[3]
        if heroes[hero]['mp'] >= mp_needed:
            heroes[hero]['mp'] -= mp_needed
            mp_left = heroes[hero]['mp']
            print(f"{hero} has successfully cast {spell_name} and now has {mp_left} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif command == 'TakeDamage':
        hero, damage, attacker = tokens[1], int(tokens[2]), tokens[3]
        heroes[hero]['hp'] -= damage
        current_hp = heroes[hero]['hp']
        if heroes[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif command == 'Recharge':
        hero, amount = tokens[1], int(tokens[2])
        amount_recovered = str()
        if heroes[hero]['mp'] + amount > 200:
            amount_recovered = 200 - heroes[hero]['mp']
            heroes[hero]['mp'] = 200
        else:
            amount_recovered = amount
            heroes[hero]['mp'] += amount
        print(f"{hero} recharged for {amount_recovered} MP!")
    elif command == 'Heal':
        hero, hp_amount = tokens[1], int(tokens[2])
        amount_recovered = int()
        if heroes[hero]['hp'] + hp_amount > 100:
            amount_recovered = 100 - heroes[hero]['hp']
            heroes[hero]['hp'] = 100
        else:
            amount_recovered = hp_amount
            heroes[hero]['hp'] += hp_amount
        print(f"{hero} healed for {amount_recovered} HP!")

for hr in heroes.keys():
    print(f"{hr}")
    print(f"  HP: {heroes[hr]['hp']}")
    print(f"  MP: {heroes[hr]['mp']}")