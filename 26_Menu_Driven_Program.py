#Menu Driven Program (cm → ft, km → miles, USD → INR)

while True:
    print("\n-----MENU-----")
    print("1. cm to ft ")
    print("2. kl to miles ")
    print("3. usd to inr ")
    print("4. exit ")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        cm  = float(input("Enter Length(cm): "))
        ft = cm/30.48
        print("Length in feet : ", ft)
    
    elif choice == 2:
        km = float(input("Enter Distance(Km): "))
        miles = km * 0.6214
        print("Distance in Miles: ", miles)
    
    elif choice == 3:
        usd = float(input("Enter Amount(usd): "))
        inr = usd * 94
        print("Amount in Indian Rupees: ", inr)
    
    elif choice == 4:
        print("Exit")
        break
    
    else:
        print("Invalid Choice")
    