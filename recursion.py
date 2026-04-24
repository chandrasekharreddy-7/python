# def recursion(n):
#     if n == 1:
#         return 1
#     else:
#         return 1 + recursion(n // 10)
# i = int(input("enter integer :"))
# print(f"total no of digits = {recursion(i)}")


def coin_change(amount, coin):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if coin == 0:
        return 0
    if coin == 5:
        return coin_change(amount - 5,5) + coin_change(amount, 2)
    elif coin == 2:
        return coin_change(amount - 2,2) + coin_change(amount, 1)
    else:
        return coin_change(amount - 1,1)
amount = 6
print(f"no of ways : {coin_change(amount, 5)}")