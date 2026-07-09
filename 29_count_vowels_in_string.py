str = input("enter string: ")
vowel = ["a","e","i","o","u","A","E","I","O","U"]
count = 0
for s in str:
    if s in vowel:
        count += 1
print(count)