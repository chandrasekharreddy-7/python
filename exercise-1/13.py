''' Q13 : Write a program that takes an integer as input and checks if it is divisible by 17. '''
''' PROCESS - 1 '''
number = int(input("enter a number :"))
divisible = int(input("enter a number to check divisble or not :"))
if number % divisible == 0:
    print(f"entered number {number} is divisible with {divisible}")
else:
    print(f"entered number {number} is not divisible with {divisible}")


''' PROCESS - 2 '''
def divisibilitycheck(number,divisor):
    if number % divisor == 0:
        print(f"entered number {number} is divisible with {divisor}")
    else:
        print(f"entered number {number} is not divisible with {divisor}")
number = int(input("enter a number :"))
divisor = int(input(f"enter a divisor to check divisble or not {number} :"))
divisibilitycheck(number,divisor)