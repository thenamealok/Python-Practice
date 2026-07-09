str = input("enter string: ").lower()
reverse = ""
for i in range(len(str)-1, -1, -1):
    reverse += str[i]

if reverse == str:
    print("Yes, given String is palindrome.")
else:
    print("No, given String is not palindrome.")