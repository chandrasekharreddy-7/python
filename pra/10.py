''' Armstrong Number:
    Write a function cubesum to return the sum of the cubes of individual digits and 
    use it in another function isArmstrong to check if a 3-digit number is an Armstrong number. '''
def cube_sum(num):
    s = 0
    while num > 0:
        r = num % 10
        s += r ** 3
        num //= 10
    return s
def is_armstrong(num):
    c = cube_sum(num)
    if c == num:
        return f"{num} is an armstrong number."
    return f"{num} is not an armstrong number."
num = int(input("enter number to check armstrong or not :"))
print(is_armstrong(num))