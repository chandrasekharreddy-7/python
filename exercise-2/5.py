''' Q5. Write a program that takes as input n1 o1 n2 o2 n3, where n1, n2, n3 are natural numbers
        and o1, o2 ∈ {+, -, *}. Use nested if--else--if statements to evaluate the expression. '''
''' process - 1 '''
n1 = input("Enter a natural number: ")
n2 = input("Enter a natural number: ")
n3 = input("Enter a natural number: ")
op1 = input("Enter your choice for operation 1 (+ / - / *): ")
op2 = input("Enter your choice for operation 2 (+ / - / *): ")
if n1.isdigit() and float(n1) > 0:
    n1 = float(n1)
    if n2.isdigit() and float(n2) > 0:
        n2 = float(n2)
        if n3.isdigit() and float(n3) > 0:
            n3 = float(n3)
            if op1 in ["+", "-", "*"]:
                if op2 in ["+", "-", "*"]:
                    if op1 == '+':
                        if op2 == '+':
                            result = n1 + n2 + n3
                        elif op2 == '-':
                            result = n1 + n2 - n3
                        elif op2 == '*':
                            result = n1 + n2 * n3
                    elif op1 == '-':
                        if op2 == '+':
                            result = n1 - n2 + n3
                        elif op2 == '-':
                            result = n1 - n2 - n3
                        elif op2 == '*':
                            result = n1 - n2 * n3
                    elif op1 == '*':
                        if op2 == '+':
                            result = n1 * n2 + n3
                        elif op2 == '-':
                            result = n1 * n2 - n3
                        elif op2 == '*':
                            result = n1 * n2 * n3
                    print(f"Result = {result}")
                else:
                    print("Please enter correct option from (+ / - / *) for op2.")
            else:
                print("Please enter correct option from (+ / - / *) for op1.")
        else:
            print("Please enter a natural number for n3.")
    else:
        print("Please enter a natural number for n2.")
else:
    print("Please enter a natural number for n1.")


''' process - 2 '''
def evaluate_expression(n1, op1, n2, op2, n3):
    result = None
    if op1 == '+':
        if op2 == '+':
            result = n1 + n2 + n3
        elif op2 == '-':
            result = n1 + n2 - n3
        elif op2 == '*':
            result = n1 + n2 * n3
    elif op1 == '-':
        if op2 == '+':
            result = n1 - n2 + n3
        elif op2 == '-':
            result = n1 - n2 - n3
        elif op2 == '*':
            result = n1 - n2 * n3
    elif op1 == '*':
        if op2 == '+':
            result = n1 * n2 + n3
        elif op2 == '-':
            result = n1 * n2 - n3
        elif op2 == '*':
            result = n1 * n2 * n3
    return result
n1 = input("enter a natural number :")
n2 = input("enter a natural number :")
n3 = input("enter a natural number :")
op1 = input("enter your choice for operation 1 (+ / - / *) :")
op2 = input("enter your choice for operation 2 (+ / - / *) :")
if n1.isdigit() and float(n1) > 0:
    n1 = float(n1)
    if n2.isdigit() and float(n2) > 0:
        n2 = float(n2)
        if n3.isdigit() and float(n3) > 0:
            n3 = float(n3)
            if op1 == "+" or op1 == "-" or op1 == "*":
                if op2 == "+" or op2 == "-" or op2 == "*":
                    print(f"result = {evaluate_expression(n1, op1, n2, op2, n3)}")
                else:
                    print("please enter correct option from (+ / - / *) for o2.")
            else:
                print("please enter correct option from (+ / - / *) for o1.")
        else:
            print("please enter a natural number for n3.")
    else:
        print("please enter a natural number for n2.")
else:
    print("please enter a natural number for n1.")