''' Q2 . Write a program to check whether a number has 0 as its last digit. '''
a = input("enter an integer(to check last digit is 0) :")
if a.isdigit():
    a = int(a)
    remainder = a % 10
    if remainder == 0:
        print(f"the number {a} has last digit 0")
    else:
        print(f"the number {a} had not 0 as last digit.")
else:
    print("please enter a number.")


''' process - 2 '''
def check_last_digit_zero(a):
    if a.isdigit():
        a = int(a)
        remainder = a % 10
        if remainder == 0:
            return f"The number {a} has last digit 0."
        else:
            return f"The number {a} does not have 0 as last digit."
    else:
        return "Please enter a number."
a = input("Enter an integer (to check last digit is 0): ")
print(check_last_digit_zero(a))