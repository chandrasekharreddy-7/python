''' Write a program that takes an integer as input, and displays whether this integer is negative,
positive, or zero. '''
''' PROCESS - 1 '''
integer = int(input("enter an integer(to check negative, positive, or zero ) :"))
if integer == 0:
    print("entered number is 0.")
elif integer < 0:
    print(f"entered integer {integer} is negative.")
elif integer > 0:
    print(f"entered integer {integer} is positive.")
else :
    print("please enter an integer.")


''' PROCESS - 2 '''
def integercheck(number):
    if number == 0:
        print("entered integer is 0.")
    elif number < 0:
        print(f"entered integer {number} is negative")
    elif number > 0:
        print(f"entered integer {number} is positive.")
    else :
        print("please enter an integer.")
number = int(input("enter an integer (to check negative, positive, or zero) :"))
integercheck(number)