def check_triangle_validity():
    angle1 = int(input("Enter First angle value: "))
    angle2 = int(input("Enter Second angle value: "))
    angle3 = int(input("Enter Third angle value: "))

    if (angle1 + angle2 + angle3 == 180) and (angle1 > 0 and angle2 > 0 and angle3 > 0):
        return "Yes, the given angles form a valid triangle."
    else:
        return "No, the given angles do not form a valid triangle."
    
print(check_triangle_validity())