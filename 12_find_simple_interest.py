def find_simple_interest():
    p = int(input("Enter Principle Amount: "))
    r = int(input("Enter rate: "))
    t = int(input("Enter time in year: "))

    si = (p*r*t)/100
    return si

s_i_ = find_simple_interest()
print("Simple Interest = ", s_i_)