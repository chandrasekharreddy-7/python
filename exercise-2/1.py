''' Q1 : Write a program to swap two integers without using a third variable. '''
''' process - 1 '''
a = int(input("enter 1st integer to swap :"))
b = int(input("enter 2nd integer to swap :"))
a = a ^ b
b = a ^ b
a = a ^ b
print(a ,b)


''' process - 2 '''
def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
a = int(input("Enter 1st integer to swap: "))
b = int(input("Enter 2nd integer to swap: "))
a, b = swap_numbers(a, b)
print(a, b)