print("1 Make an order")
print("2 List all user orders")
print("3 Request help with an order")
print("4 Request to cancel an order")
print("0 Exit the main menu and the program")

while True:
    print("\nPlease select an option:")
    sel=input()
    if sel=='0' or sel=='1' or sel=='2' or sel=='3' or sel=='4':
        break
    else:
        print("Please enter a valid number form 0 to 4")
        continue


#Make an order
