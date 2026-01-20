happiness_list = list(map(int, input().split()))
factor = int(input())

mapped_happiness = list(map(lambda x: x * factor, happiness_list))

average_happiness = sum(mapped_happiness)/len(mapped_happiness)


happy_count = list(filter(lambda a: a>= average_happiness, mapped_happiness))

if len(happy_count)>=(len(mapped_happiness)/2):
    print(f"Score: {len(happy_count)}/{len(mapped_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(mapped_happiness)}. Employees are not happy!")