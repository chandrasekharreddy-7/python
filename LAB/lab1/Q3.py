def sum_of_cubes(n):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total
def is_armstrong(n):
    if n == sum_of_cubes(n):
        return f"{n} is an Armstrong Number"
    else:
        return f"{n} is not an Armstrong Number"
num = int(input("enter a three digit integer :"))
print(is_armstrong(num))