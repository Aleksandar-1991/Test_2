key=int(input())
lines=int(input())

word=str()

for line in range(lines):
    char=input()
    newchar=chr(ord(char)+key)
    word += newchar

print(word)