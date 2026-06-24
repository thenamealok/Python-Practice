#Without Using Third Variable
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
print("Numbers Before Swap : ", num1, num2)
num1, num2 = num2, num1
print("Numbers After Swap : ", num1, num2)