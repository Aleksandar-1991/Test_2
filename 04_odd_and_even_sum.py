n = input()

def sum_odd_even(full_string: str) -> list:
    odd_sum=0
    even_sum=0

    for i in full_string:
        if int(i)%2==0:
            even_sum += int(i)
        else:
            odd_sum += int(i)

    return odd_sum, even_sum

sum_odd, sum_even = sum_odd_even(n)

print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")

