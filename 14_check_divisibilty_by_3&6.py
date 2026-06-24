def divisibility_of_6and3():
    num = int(input("Enter a Number : "))
    if num % 3 == 0 and num % 6 == 0:
        return "Number is divisible by both 3 and 6."
    else:
        return "Number is not divisible by both 3 and 6."
    
print(divisibility_of_6and3())