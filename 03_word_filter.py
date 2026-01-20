initial_list = input().split()

new_list = [word for word in initial_list if len(word)%2==0]

print("\n".join(new_list))
