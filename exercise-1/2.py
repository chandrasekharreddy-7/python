''' Write a program that takes two integers a and b as input and prints their sum, difference,
product, quotient, and remainder. '''
a = int(input("enter 1st integer :"))
b = int(input("enter 2nd integer :"))
sum = a + b
diff = a - b
pro = a * b
print(f"sum of {a} and {b} = {sum}")
print(f"difference of {a} and {b} = {diff}")
print(f"product of {a} and {b} = {pro}")
if b == 0:
    print("0 is in denominator., quotient undefined.")
else:
    print(f"quotient of {a} and {b} = {a/b}")
if b == 0:
    print("0 is in denominator., remainder undefined.")
else:
    print(f"remainder of {a} and {b} = {a%b}")


''' process - 2 '''
def asmd(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    pro = num1 * num2
    if num2 != 0:
        quo = num1 / num2
        rem = num1 % num2
    else:
        quo = "undefined!"
        rem = "undefined!"
        print("remainder ahd quotient are undefined with zero as denominator.")
    return f"sum  = {add}\ndifference = {sub}\nproduct = {pro}\nquotient = {quo}\nremainder = {rem}"
num1 = int(input("enter 1st integer :"))
num2 = int(input("enter 2nd integer :"))
print(asmd(num1, num2))