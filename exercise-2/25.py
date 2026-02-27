''' Q25 : Write a program that takes a number between 0 and 65535 and prints its hexadecimal
representation. Note: Do not use the hex function. '''
''' process - 1 '''
num = int(input("Enter a number between 0 and 65535: "))
if 0 <= num <= 65535:
    hex_digits = "0123456789ABCDEF"
    hex_representation = ""
    while num > 0:
        remainder = num % 16
        hex_representation = hex_digits[remainder] + hex_representation
        num //= 16
    if hex_representation == "":
        hex_representation = "0"
    print(f"The hexadecimal representation is: {hex_representation}")


''' process - 2 '''
def decimal_to_hex(num):
    if num < 0:
        return "Please enter a non-negative number."
    hex_digits = "0123456789ABCDEF"
    hex_representation = ""
    if num == 0:
        return "The hexadecimal representation is: 0"
    while num > 0:
        remainder = num % 16
        hex_representation = hex_digits[remainder] + hex_representation
        num //= 16
    return f"The hexadecimal representation is: {hex_representation}"
num = int(input("Enter a number: "))
print(decimal_to_hex(num))