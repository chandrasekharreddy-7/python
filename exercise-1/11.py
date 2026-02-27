
''' Q11 : Write a program that takes an integer as input and displays if it is odd or even. '''
''' PROCESS - 1 '''
number = int(input("enter a number (to check even or odd or zero) :"))
if number == 0:
    print("0 is neither even nor odd.")
elif number % 2 == 0:
    print(f"{number} is even")
else :
    print(f"{number} is odd.")


''' PROCESS - 2 '''
def evenorodd(number):
    if number == 0:
        print("0 is neither even nor odd.")
    elif number % 2 == 0:
        print(f"{number} is even")
    else :
        print(f"{number} is odd.")
number = int(input("enter a number (to check even or odd or zero) :"))
evenorodd(number)