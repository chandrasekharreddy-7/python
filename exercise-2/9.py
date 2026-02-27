
''' Q9 . Write a program that takes as input the cost price and selling price of an item, prints whether
        the sale resulted in a profit or a loss, and prints the amount. '''
''' process - 1 '''
costprice = input("Enter cost price of the item: ")
sellprice = input("Enter sell price of the item: ")
profit = 0
loss = 0
if costprice.isdigit() and int(costprice) >= 0:
    costprice = int(costprice)
    if sellprice.isdigit() and int(sellprice) >= 0:
        sellprice = int(sellprice)
        if costprice > sellprice:
            loss = costprice - sellprice
            print(f"You got a loss of {loss} rupees.")
        elif costprice < sellprice:
            profit = sellprice - costprice
            print(f"You got a profit of {profit} rupees.")
        else:
            print("You did not make any profit or loss on the item.")
    else:
        print("Please enter a correct selling price.")
else:
    print("Please enter a correct cost price.")


''' process - 2 '''
def amountcalculator(costprice, sellprice):
    profit = 0
    loss = 0
    if costprice.isdigit() and int(costprice) >= 0:
        costprice = int(costprice)
        if sellprice.isdigit() and int(sellprice) >= 0:
            sellprice = int(sellprice)
            if costprice > sellprice:
                loss = abs(costprice - sellprice)
                print(f"you got a loss of {loss}.rupees")
            elif costprice < sellprice:
                profit = abs(costprice - sellprice)
                print(f"you got a profit of {profit}.rupees")
            else:
                print("you doesn't make any profit or loss on the item.")
        else:
            print("please enter a correct selling price.")
    else:
        print("please enter a correct cost price")
costprice = input("enter cost price of the item :")
sellprice = input("enter sell price of the item :")
amountcalculator(costprice, sellprice)