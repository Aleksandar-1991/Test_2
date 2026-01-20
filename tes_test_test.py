a = "hello world, hello Python"  # string
s = "hello"  # substring
x = a.find(s)

if x != -1:
    y = a.find(s, x + 1)
    if y != -1:  # index of second occurrence
        print(y)
    else:
        print(-1)
else:
    print(-1)

#print(x)