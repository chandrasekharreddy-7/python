''' Write a program that takes two integers a and b as input and displays whether a < b, a = b,
or a > b. '''
''' PROCESS - 1 '''
a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
print(f"relation between {a} and {b} is :")
if a > b:
    print(f"result : {a} > {b}")
elif a < b:
    print(f"result : {a} < {b}")
elif a == b:
    print(f"result : {a} = {b}")
else :
    print("please enter number in both a and b")

''' PROCESS - 2 '''
def equitycheck(a,b):
    if a > b:
        print(f"relation : {a} > {b}.")
    elif a < b:
        print(f"result : {a} < {b}")
    elif a == b:
        print(f"result : {a} = {b}")
    else :
        print("please enter number in both a and b")
a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
equitycheck(a,b)