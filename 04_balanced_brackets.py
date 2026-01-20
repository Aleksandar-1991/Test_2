lines=int(input())


opening_bracket=False
closing_bracket=False
balanced=bool

for line in range(lines):
    word=input()
    if word=="(" and opening_bracket==True:
        balanced=False
        break
    elif word=="(" and opening_bracket==False:
        opening_bracket=True
    elif word==")" and opening_bracket==True:
        opening_bracket=False
        balanced=True
    elif word==")" and opening_bracket==False:
        balanced=False
        break

if balanced==True:
    print("BALANCED")
else:
    print("UNBALANCED")
