'''Q12 : Write a program that takes a floating-point value as input and prints its absolute value. '''
num = float(input("enter any floating-point number :"))
if num < 0:
    print(f"absolute value of {num} is {-num}")
else:
    print(f"absolute value of {num} is {num}")