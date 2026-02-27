''' Write a program that takes the radius of a circle as input and computes its area.
Note: If the radius is non-negative, display an appropriate message. '''
r = float(input("enter radius of circle :"))
if r >= 0:
    pi = 3.14
    area = pi * r * r
    print(f"area of circle = {area:.2f}")
else:
    print("radius is in non - negative.")


'''process -2'''
def areaofcircle(radius):
    pi = 3.14
    if radius < 0:
        return "radius is non - negative."
    else:
        area = pi * radius * radius
        return f"area of circle with radius '{radius}' = {area}"
radius = int(input("enter the radius of circle :"))
areaofcircle(radius)