n = int(input())

def print_loading_bar(num: int) -> str:
    if n == 100:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        loaded = num//10
        print(f"{num}% [{'%' * loaded}{'.' * (10-loaded)}]\nStill loading...")


print_loading_bar(n)

