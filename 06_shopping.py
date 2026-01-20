budget=int(input())

while budget>=0:
    product=input()
    if product=="End" and budget>=0:
        print("You bought everything needed.")
        break
    budget-=int(product)
    if budget<0:
        print("You went in overdraft!")
        break

