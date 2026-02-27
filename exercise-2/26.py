''' Q26 : Write a program that takes a number between 0 and 31 and prints its binary representation.
Note: Do not use the bin function. '''
i = int(input("enter a number :"))
string = ""
reverse = ""
if i == 0:
    n = 0
    print(f"binary equivalent = {n}")
else: 
    while i > 0:
            n = i % 2
            string += str(n)
            i = i // 2
for i in range(len(string)+1):
    reverse = string[::-1]
print(f"binary equivalent = {reverse}")


''' process - 2 '''
def decimal_to_binary(num):
    if num < 0:
        return "Please enter a non-negative number."
    if num == 0:
        return "Binary equivalent = 0"
    string = ""
    while num > 0:
        n = num % 2
        string += str(n)
        num //= 2
    reverse = string[::-1]
    return f"Binary equivalent = {reverse}"
num = int(input("Enter a number: "))
print(decimal_to_binary(num))