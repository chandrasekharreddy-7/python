''' Q8 : Write a program that takes a three-digit integer as input and prints the sum of its digits. '''
''' PROCESS - 1 '''
num = int(input("enter any integer number :"))
org_num = num
sum = 0
while num > 0:
    remainder = num % 10
    sum = sum + remainder
    num = num // 10
print(f"sum of digits in {org_num} = {sum}")


''' PROCESS - 2 '''
def sumofdigits(num):
    org_num = num
    sum = 0
    while num > 0:
        remainder = num % 10
        sum = sum + remainder
        num = num // 10
    return sum
num = int(input("enter any integer number :"))
print(f"sum of digits in {num} = {sumofdigits(num)}")