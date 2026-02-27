''' Q6 . Write a program that takes as input two integers and prints appropriate messages if at least
        one or both are positive, negative, or zero. '''
a = input("enter 1st integer :")
b = input("enter 2nd integer :")
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if a > 0 and b > 0:
        print(f"In {a} and {b}, both are positive.")
    elif a > 0 and b < 0:
        print(f"In {a} and {b}, {a} is positive and {b} is negative.")
    elif a < 0 and b < 0:
        print(f"In {a} and {b}, both are negative.")
    elif a < 0 and b == 0:
        print("a is negative, b is zero.")
    elif a > 0 and b == 0:
        print("a is positive, b is zero.")
    elif a == 0 and b > 0:
        print("a is zero, b is positive.")
    else:
        print("a is zero, b is negative.")
else:
    print("please enter a number.")