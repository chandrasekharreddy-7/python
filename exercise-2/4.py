''' Q4 . Write a program that takes a natural number as input and prints the remainder when it is
         divided by 3. '''
''' process - 1 '''
a = input("enter a natural number :")
if a.isdigit():
    a = int(a)
    if a > 0:
        x = a % 3
        print(f"remainder when divided by 3 = {x}")
else:
    print("enter a number")


''' process - 2 '''
def remainder_by_three(a):
    if a.isdigit():
        a = int(a)
        if a > 0:
            x = a % 3
            return f"Remainder when divided by 3 = {x}"
        else:
            return "Please enter a natural number."
    else:
        return "Enter a number."
a = input("Enter a natural number: ")
print(remainder_by_three(a))