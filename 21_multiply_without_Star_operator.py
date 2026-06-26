#Write a program that can multiply 2 numbers provided by the user without using the * operator

a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))

total = 0
for i in range(b):
    total += a

print(f"Multiplication of two numbers {a} and {b} without * operator = ", total)