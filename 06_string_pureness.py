n=int(input())
characters=[".", ",", "_"]

for i in range(n):
    string=input()
    if any(char in string for char in characters ):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")




        # for i in range(n):
        #     string=input()
        #     if characters in string:
        #         print(f"{string} is not pure!")
        #     else:
        #         print(f"{string} is pure.")