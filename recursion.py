def recursion(n):
    if n == 1:
        return 1
    else:
        return 1 + recursion(n // 10)
i = int(input("enter integer :"))
print(f"total no of digits = {recursion(i)}")