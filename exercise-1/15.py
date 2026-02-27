''' Q15 : Write a program to select one option from the list and display output accordingly.
Example:
Please enter your choice:
1. Check Balance
2. View Offers
3. Special Recharge
Enter 0 to exit
(Display some arbitrary message for each option, e.g., “Your balance is Rs. 500”.) '''
''' *****   ATM PROGRAM   ***** '''
''' process - 1 '''
balance = 5000
print("Please enter your choice:")
print("1. Check Balance")
print("2. credit money")
print("3. debit money")
print("4. View offers")
print("5. Special Recharge")
print("PRESS '0' TO EXIT")
c = int(input("enter your choice from above options :"))
if c == 1:
    print(f"your current balance = {balance}.")
elif c == 2:
    newbalance = 0
    credit = int(input("enter money you want to credit :"))
    newbalance = balance + credit
    print(f"new balance after credit of {credit} rupees = {newbalance}")
elif c == 3:
    newbalance = 0
    debit = int(input("enter money you want to debit :"))
    if debit > balance:
        print("your current balance is less than your debiting ammount.")
    else:
        newbalance = balance - debit
        print(f"new balance after debit of {debit} rupees = {newbalance}")
elif c == 4:
    print("YOU CAN VIEW OUR RESPECTIVE BANK OFFERS.")
elif c == 5:
    print("steps to SPECIAL RECHARGE.")
elif c == 0:
    print("YOU LOGGED OUT FROM ATM.")
else :
    print("please enter correct choice.")


''' process - 2 '''
def atm_machine():
    balance = 5000
    print("Please enter your choice:")
    print("1. Check Balance")
    print("2. Credit Money")
    print("3. Debit Money")
    print("4. View Offers")
    print("5. Special Recharge")
    print("PRESS '0' TO EXIT")
    c = int(input("Enter your choice from above options: "))
    if c == 1:
        print(f"Your current balance = {balance}")
    elif c == 2:
        credit = int(input("Enter money you want to credit: "))
        balance += credit
        print(f"New balance after credit of {credit} rupees = {balance}")
    elif c == 3:
        debit = int(input("Enter money you want to debit: "))
        if debit > balance:
            print("Your current balance is less than your debiting amount.")
        else:
            balance -= debit
            print(f"New balance after debit of {debit} rupees = {balance}")
    elif c == 4:
        print("You can view our respective bank offers.")
    elif c == 5:
        print("Steps to Special Recharge.")
    elif c == 0:
        print("You logged out from ATM.")
    else:
        print("Please enter correct choice.")
atm_machine()