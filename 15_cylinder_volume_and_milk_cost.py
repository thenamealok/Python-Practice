def cylinder_volume_and_milk_cost():
    r = int(input("Enter the radius of Cylinder: "))
    h = int(input("Enter the height of Cylinder: "))
    volume  = (22/7)*(r**2)*h
    litres = volume/1000
    cost = 40*litres
    return volume, litres, cost
volume, litres, cost = cylinder_volume_and_milk_cost()
print(f"Volume of Cylinder = {volume:.2f} cm³")
print(f"Milk = {litres:.2f} litres")
print(f"Cost = ₹{cost:.2f}")