''' Q23 : Write a program that takes three integers x, y, z and checks the divisibility of x by y and z,
printing appropriate messages. '''
x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
z = int(input("Enter the third integer (z): "))
if y != 0 and z != 0:
    if x % y == 0 and x % z == 0:
        print(f"{x} is divisible by both {y} and {z}.")
    elif x % y == 0:
        print(f"{x} is divisible by {y} but not by {z}.")
    elif x % z == 0:
        print(f"{x} is divisible by {z} but not by {y}.")
    else:
        print(f"{x} is not divisible by either {y} or {z}.")
else:
    print("Please enter non-zero integers for y and z to check divisibility.")