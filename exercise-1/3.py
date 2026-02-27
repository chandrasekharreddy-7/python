''' Write a simple calculator program. It should be able to add, subtract, multiply, and divide
any two numbers input by the user.
Note: The user will also specify the operation to perform. '''
''' PROCESS - 1 '''
a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
print("you can perform below operations on entered two numbers.")
print("1. ADDITION")
print("2. DIFFERENCE")
print("3. PRODUCT")
print("4. DIVISION")
c = int(input("enter your choice from above options :"))
if c == 1:
    sum = a + b
    print(f"sum of {a} and {b} = {sum}")
elif c == 2:
    difference = a - b
    print(f"difference of {a} and {b} = {difference}")
elif c == 3:
    product = a * b
    print(f"product of {a} and {b} = {product}")
elif c == 4:
    division = a / b
    print(f"division of {a} and {b} = {division}")
else:
    print("please enter correct choice.")


''' PROCESS - 2 '''
num1 = int(input("enter 1st integer :"))
num2 = int(input("enter 2nd integer :"))
print("you can perform below operations on entered two numbers.")
print("1. ADDITION")
print("2. DIFFERENCE")
print("3. PRODUCT")
print("4. DIVISION")
c = int(input("enter your choice from above options :"))
match(c):
    case 1:
        sum = num1 + num2
        print(f"sum of num1 and num2 = {sum}")
    case 2:
        difference = num1 - num2
        print(f"difference of num1 and num2 = {difference}")
    case 3:
        product = num1 * num2
        print(f"product of num1 and num2 = {product}")
    case 4:
        try:
            division = num1 / num2
            division1 = num1 // num2
            print(f"division of num1 and num2 = {division}")
            print(f"division(int) of num1 and num2 = {division1}")
        except :
            print("division by zero is undefined.")
    case _:
        print("please enter correct choice.")


''' process - 3 '''
def simple_calculator(num1, num2):
    while True:
        print("=====   SIMPLE CALCULATOR   =====")
        print("1. Addition (add,Add,ADD,+)")
        print("2. Subtaction (subtract,Subtract,SUBTRACT,-)")
        print("3. Multiplication (multiplication,Multiplication,MULTIPLICATION,*)")
        print("4. Division (division,Division,DIVISION,/)")
        option = input("enter your option from above.").lower()
        if option in ["add","Add","ADD","+","1"]:
            result = num1 + num2
            print(f"Sum of {num1} and {num2} = {result}")
        elif option in ["subtract","-","2"]:
            result = num1 - num2
            print(f"Difference of {num1} and {num2} = {result}")
        elif option in ["multiplication","*","3"]:
            result = num1 * num2
            print(f"Product of {num1} and {num2} = {result}")
        elif option in ["division","/","4"]:
            if num2 == 0:
                 print("Division is undefined!")
            else:
                result = num1 / num2
                print(f"Division of {num1} and {num2} = {result:.4f}")
        else:
            return f"Invalid input!."
        choice = input("Enter 1 to continue and 0 to exit: ")
        if choice == "0":
            print("calculator closed!.")
            break
num1 = int(input("enter 1st integer :"))
num2 = int(input("enter 2nd integer :"))
simple_calculator(num1, num2)