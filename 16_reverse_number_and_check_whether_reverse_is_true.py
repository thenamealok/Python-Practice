num = int(input("Enter a Number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num //= 10
print("Number after reversing: ", reverse)

if original == reverse:
    print("After reverse both are same.")
else:
    print("After reverse both are not same.")
