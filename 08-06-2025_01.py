gpu_price=int(input())
connector=int(input())
gpu_consumption_per_day=float(input())
profit_gpu=float(input())
hardware=1000+(13*gpu_price)+(13*connector)
total_sum=float()
days_to_return_investment=float()
total_sum=hardware

while total_sum>=0:
    total_sum+=(13*gpu_consumption_per_day)-(13*profit_gpu)
    days_to_return_investment+=1

print(hardware)
print(f"{round(days_to_return_investment)}")