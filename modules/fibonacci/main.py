from modules.fibonacci.core import create_sequence, locate

seq = None
while (user_input := input()) != "Stop":
    num = int(user_input.split()[-1])
    if user_input.startswith("Locate"):
        if not seq:
            print("Please first create a sequence!")
            continue
        print(f"{locate(seq, num)}")
    elif user_input.startswith("Create"):
        seq = create_sequence(num)
        print(*seq)
