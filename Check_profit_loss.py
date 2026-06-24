def check_profit_loss():
    CP = int(input("Enter Cost Price: "))
    SP = int(input("Enter Selling Price: "))

    if SP > CP:
        return "Profit"
    elif SP < CP:
        return "Loss"
    else:
        return "No profit and No Loss because Both Selling Price and Cost Price are equal "
    
print(check_profit_loss())
