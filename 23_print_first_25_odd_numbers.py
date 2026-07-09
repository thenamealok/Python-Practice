count = 0
for i in range(1,50,2):
    if i % 2 != 0:
        print(i)
        count += 1
        if count == 25:
            break

#other way

#for i in range(1,50,2):
#   print(i)