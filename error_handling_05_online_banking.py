class MoneyNotEnoughError(Exception):
    pass
class PINCodeError(Exception):
    pass
class UnderageTransactionError(Exception):
    pass
class MoneyIsNegativeError(Exception):
    pass

pin_code, initial_balance, age = input().split(", ")
initial_balance = int(initial_balance)
age = int(age)
MINIMAL_AGE = 18

while (transaction := input()) != "End":
    command = transaction.split("#")[0]
    money = int(transaction.split("#")[1])
    if command == "Send Money":
        given_pin_code = transaction.split("#")[2]
        if money > initial_balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if given_pin_code != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < MINIMAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        initial_balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {initial_balance:.2f} money left in the bank account")

    elif command == "Receive Money":
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        incoming_amount = money/2
        initial_balance += incoming_amount
        print(f"{incoming_amount:.2f} money went straight into the bank account")
