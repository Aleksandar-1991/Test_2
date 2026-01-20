import math

cpus_needed=int(input())
staff=int(input())
days=int(input())
profit=float()
losses=float()

if ((staff*8*days)/3)>=cpus_needed:
    cpus_made=math.floor((staff*8*days)/3)
    cpus_excess=cpus_made-cpus_needed
    profit=cpus_excess*110.10
    print(f"Profit: -> {profit:.2f} BGN")
else:
    cpus_made = math.floor((staff * 8 * days) / 3)
    cpus_less =cpus_needed - cpus_made
    losses = cpus_less * 110.10
    print(f"Losses: -> {losses:.2f} BGN")