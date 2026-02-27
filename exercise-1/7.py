''' Write a program that takes three integers as input and prints their maximum value. '''
''' PROCESS - 1 '''
a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
c = int(input("enter the 3rd number :"))
if a >= b and a >= c:
    print(f"{a} is maximum in {a},{b} and {c}")
elif b >= a and b >= c:
    print(f"{b} is maximum in {a},{b} and {c}")
elif c >= a and c >= b:
    print(f"{c} is maximum in {a},{b} and {c}")
else :
    print("enter three integers only.")


''' PROCESS - 2 '''
def maxofthree(a,b,c):
    if a >= b and a >= c:
        print(f"{a} is maximum in {a},{b} and {c}")
    elif b >= a and b >= c:
        print(f"{b} is maximum in {a},{b} and {c}")
    elif c >= a and c >= b:
        print(f"{c} is maximum in {a},{b} and {c}")
    else :
        print("enter three integers only.")
a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
c = int(input("enter the 3rd number :"))
maxofthree(a,b,c)