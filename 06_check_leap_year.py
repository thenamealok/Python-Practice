def Check_Leap_Year():
    year = int(input("Enter Year : "))
    if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)):
        return f"Given Year {year} is a Leap Year"
    else:
        return f"Given Year {year} is not a Leap Year"
    
Check = Check_Leap_Year()
print(Check)