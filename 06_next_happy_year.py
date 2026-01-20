year=input()

def check_happy_year(given_year):
    happy_year = True
    for i in given_year:
        if given_year.count(i) > 1:
            happy_year = False
            break
    return happy_year


while True:
    year=str(int(year) + 1)
    if check_happy_year(year)==True:
        print(year)
        break
    else:
        continue




