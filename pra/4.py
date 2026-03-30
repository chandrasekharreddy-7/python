''' Coordinate Geometry:
    Write a program that takes the center of a circle $(c_{x},c_{y})$, a radius $r$,
    and a point $P(p_{x},p_{y})$, and determines if the point lies inside, on, or outside the circle. '''
def check_using_circle(x, y, r, x1, y1):
    distance = ((x - x1) ** 2 + (y - y1)**2)**0.5
    if r == distance:
        return f"{(x1,y1)} lies on the circle"
    elif r < distance:
        return f"{(x1,y1)} lies outside the circle"
    else:
        return f"{(x1,y1)} lies inside the circle"
x,y = map(float, input("enter the center of circle (x, y) : ").split(","))
r = float(input("enter the radius of the circle :"))
x1, y1 = map(float, input("enter the point (x1, y1) : ").split(","))
print(check_using_circle(x, y, r, x1, y1))