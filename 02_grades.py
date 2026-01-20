def print_grade(num):
    if 2.00 <= num <= 2.99:
        print("Fail")
    if 3.00 <= num <= 3.49:
        print("Poor")
    if 3.50 <= num <= 4.45:
        print("Good")
    if 4.50 <= num <= 5.49:
        print("Very Good")
    if 5.50 <= num <= 6.00:
        print("Excellent")

print_grade(float(input()))




