l = int(input("Enter the length of figure: "))
b = int(input("Enter the breadth of figure: "))
r = int(input("Enter the radius of figure: "))

area = (l*b) + (0.5 * 3.14 * r**2)

parameter = 2*(l + b) + (3.14 * r + 2 * r)

print("Area of the given figure is:", area)
print("Perimeter of the given figure is:", parameter)