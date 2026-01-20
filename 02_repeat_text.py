text = input()

try:
    repeat_times = int(input("Please enter how many times the text should be repeated:"))
except ValueError:
    print("Variable times must be an integer")
else:
    print( text * repeat_times)

