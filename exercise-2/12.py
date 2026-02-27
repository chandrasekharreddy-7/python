''' Q12 : Write a program that takes a point P(px, py) and determines the quadrant it lies in. Explicitly
handle the cases when the point lies on the axes or at the origin. '''
x, y = float(input("enter x coordinate of the point :")), float(input("enter y coordinate of the point :"))
if x == 0 and y == 0:
    print(f"{x, y} lies at the origin.")
elif x == 0 and (y > 0 or y < 0):
    print(f"{x, y} lies on y axis")
elif y == 0 and (x > 0 or x < 0):
    print(f"{x, y} lies on x axis")
elif x > 0 and y > 0:
    print(f"{x, y} lies in Quadrant 1")
elif x > 0 and y < 0:
    print(f"{x, y} lies in Quadrant 4")
elif x < 0 and y > 0:
    print(f"{x, y} lies in Quadrant 2")
else:
    print(f"{x, y} lies in Quadrant 3")


''' process - 2 '''
def check_position(x, y):
    if x == 0 and y == 0:
        return f"{(x, y)} lies at the origin."
    elif x == 0:
        return f"{(x, y)} lies on y axis."
    elif y == 0:
        return f"{(x, y)} lies on x axis."
    elif x > 0 and y > 0:
        return f"{(x, y)} lies in Quadrant 1."
    elif x > 0 and y < 0:
        return f"{(x, y)} lies in Quadrant 4."
    elif x < 0 and y > 0:
        return f"{(x, y)} lies in Quadrant 2."
    else:
        return f"{(x, y)} lies in Quadrant 3."
x = float(input("Enter x coordinate of the point: "))
y = float(input("Enter y coordinate of the point: "))
print(check_position(x, y))