def Check_Even_Odd():
    num = int(input("Enter Number : "))
    if num % 2 == 0:
        return f"Given Number {num} is Even"
    else:
        return f"Given Number {num} is Odd"
    return num
check = Check_Even_Odd()
print(check)