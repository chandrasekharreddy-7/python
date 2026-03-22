'''
Name: B.chandra sekhar reddy
PRN NO: 250200299

Collaborators:
    1) S.Siva Sarsha
    2) J.V.A.Siva Rama Teja
'''
while True:
    # asks user until the user enters correct input.

    try:

        Cost_of_house = float(input("enter the total cost of dream home :"))
        # user enters his dream house cost.
        if Cost_of_house > 0:
            # checks user entered cost of house.
            Down_payment = 0.25 * Cost_of_house
            # calculates downpayment of your dream house.
            savings = 0.0
            break
        else:
            print("Cost of house must be greater then 0.")

    except ValueError:

        print("invalid input!.please input correct cost.")
        # checks user entered correct value or not
while True:
    # asks user until the user enters correct input.

    try:

        annual_salary = float(input("Enter your annual salary :"))
        # asks user to enter annual salary.
        if annual_salary > 0:
            # checks user entered positive salary or not.
            monthly_salary = annual_salary / 12
            break
        else:
            print("salary must be grater than 0.")

    except ValueError:

        print("invalid input!.please input correct annual salary.")

        # checks user entered correct salary or not.

while True:
    # asks user until the user enters correct input.

    try:

        Portion_saved = float(input("Enter the percent of your annual salary to save, as a decimal (> 0 and < 1) : "))

        if 0 < Portion_saved <= 1:
            break
        else:
            print("please enter in decimal value (> 0 and < 1)")
            
    except ValueError:
        print("please enter correct portion saved annualy in percantage (0-1) :")
        # checks user entered correct portion saved or not.

while True:
    # asks user until the user enters correct input.

    try:

        Annual_return = float(input("Enter annual return on investment :"))
        if 0 <= Annual_return <= 100:
            # checks annual return is between 0 and 100.
            monthly_return = (Annual_return/100) / 12
            break
        else:
            print("please enter correct annual return (1 - 100).")

    except ValueError:

        print("please enter correct annual return on investment (1 - 100).")

        # checks user entered correct annual return.
while True:
    # asks user until the user enters correct input.

    try:
        semi_annual_rise = float(
            input("enter semi annual rise, in decimal (> 0 and <= 1) :"))
        # user enters semi annual rise.
        if semi_annual_rise > 0 and semi_annual_rise <= 1:
            # checks input is between 0 and 1.
            break
        else:
            print("please enter correct semi- annual rise (> 0 and <= 1).")
            # prints appropriate message when input is incorrect.
    except ValueError:
        print("please enter correct decimal value.")
        # prints appropriate message when value is incorrect.

months = 0
while savings < Down_payment:
    # checks condition until savings less than required down payment.
    savings += savings * monthly_return
    savings += monthly_salary * Portion_saved
    months += 1
    # add one month for each iteration.

    if months % 6 == 0:
        # checks month is divisible by 6 or 6 months is completed or not.
        annual_salary += annual_salary * semi_annual_rise
        # adds semi annual rise to annual salary.
        monthly_salary = annual_salary / 12
        # converts annual salary in to monthly salary.

print(f"no of months = {months}")     # prints no of months.
