n = int(input())

def is_perfect(num: int) -> str:
    sum_of_dividers=0
    for i in range(1,num):
        if num%i==0:
            sum_of_dividers += i
    if sum_of_dividers==num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

is_perfect(n)