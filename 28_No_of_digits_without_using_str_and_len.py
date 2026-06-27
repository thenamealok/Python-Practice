num = int(input("Enter Number: "))

if num == 0:
    print("Number of Digits = 1. ")

else:
    count = 0
    while num > 0:
        count += 1
        num //= 10
    print("Number of digits :",count)

