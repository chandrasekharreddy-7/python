''' Q16 : Write a program that takes as input the coefficients of the quadratic equation
" ax2 + bx + c = 0 " and prints whether the roots are real or complex. '''
a = int(input("give coeffecient of x square:"))     
b = int(input("give coeffecient of x:"))
c = int(input("give constant value:"))
root1 = 0
root2 = 0
d = b*b - 4 * a * c
if d > 0:
    print("the quadratic equation has real and distinct roots.")
elif d == 0:
    print("the quadratic equation has real and equal roots.")
else :
    print("the quadratic equation has complex (imaginary) roots.")
if d >= 0:
    root1 = (-b + (d**(0.5))) / 2 * a
    root2 = (-b - (d**(0.5))) / 2 * a
    print(f"Roots of the given equation is: {root1,root2}")


''' process - 2 '''
def quadratic_roots(a, b, c):
    d = b*b - 4*a*c
    if d > 0:
        print("The quadratic equation has real and distinct roots.")
    elif d == 0:
        print("The quadratic equation has real and equal roots.")
    else:
        print("The quadratic equation has complex (imaginary) roots.")
    if d >= 0:
        root1 = (-b + d**0.5) / (2 * a)
        root2 = (-b - d**0.5) / (2 * a)
        print(f"Roots of the given equation are: {root1}, {root2}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(d)**0.5) / (2 * a)
        print(f"Roots are: {real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i")
a = int(input("Give coefficient of x²: "))
b = int(input("Give coefficient of x: "))
c = int(input("Give constant value: "))
quadratic_roots(a, b, c)