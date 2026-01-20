num=float(input())

if num==0:
    print("zero")
elif num>1000000:
    print("large positive")
elif 1<=num<=1000000:
    print("positive")
elif 0<num<1:
    print("small positive")
elif -1000000 <= num <= -1:
    print("negative")
elif num>(-1) and num<0:
    print("small negative")
elif num<-1000000:
    print("large negative")
