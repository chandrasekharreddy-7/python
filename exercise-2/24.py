''' Q24 : Write a program that takes a positive integer and prints the quotient and remainder when
divided by 2. Note: Do not use / or % operators. '''
num = int(input("Enter a positive integer: "))
if num > 0: 
    quotient = num // 2
    remainder = num - (quotient * 2)
    print(f"The quotient of {num} divided by 2 is: {quotient}")
    print(f"The remainder of {num} divided by 2 is: {remainder}")