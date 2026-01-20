month=input()
hours_spent=int(input())
people=int(input())
daytime=input()
price=float()
total_sum=float()

if daytime=="day" and (month=="march" or month=="april" or month=="may"):
    price=10.5
elif daytime=="day" and (month=="june" or month=="july" or month=="august") :
    price=12.6
elif daytime=="night" and (month=="march" or month=="april" or month=="may") :
    price=8.4
elif daytime == "night" and (month == "june" or month == "july" or month == "august"):
    price=10.2

if people>=4:
    price*=0.9
if hours_spent>=5:
    price*=0.5

total_sum=people*price*hours_spent



print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_sum:.2f}")

