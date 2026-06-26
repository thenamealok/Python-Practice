#Write a program that will give you the in hand salary after 
# deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is 
# between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)
# (0-1lakh print k).

def inhand_salary_calc():
    sal = int(input("Enter Your Gross Salary(in lakhs): "))
    effective_sal = (sal - sal*(18/100))
    if sal <= 100000:
        print("k")
        net_sal = effective_sal
    elif 500000 <= sal <= 1000000:
        net_sal = effective_sal - sal*0.1
    elif 1100000 <= sal <= 2000000:
        net_sal = effective_sal - sal*0.2
    elif sal > 2000000:
        net_sal = effective_sal - sal*0.3
    else:
        net_sal = effective_sal
    return net_sal


print("Net Salary in hand after HRA, PF, DA and TAX deduction: ", inhand_salary_calc())