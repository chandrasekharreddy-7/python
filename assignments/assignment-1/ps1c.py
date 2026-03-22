
'''
Name: B.chandra sekhar reddy
PRN NO: 250200299

Collaborators:
    1) S.Siva Sarsha
    2) J.V.A.Siva Rama Teja
'''
while True:
    # asks unti the user enters correct data.
    try:
        
        annual_salary = float(input("Enter starting salary: "))
        # asks user to enter annual salary
        
        if annual_salary <= 0:
            # checks user entered salary > 0 or not.
            print("Starting salary must greater than zero.")
            continue
        break
    
    except ValueError:
        # handles the contition when it is ValueError.
        print("Invalid input! try again.")
# taking given values.
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
            continue

    except ValueError:

        print("invalid input!.please input correct cost.")
        # checks user entered correct value or not
while True:
    # asks user until the user enters correct input.

    try:

        Annual_return = float(input("Enter annual return on investment :"))
        
        if Annual_return >= 0 and Annual_return <= 100:
            # checks annual return is between 1 and 100.
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
        semi_annual_rise = float(input("enter semi annual rise, in decimal (> 0 and <= 1) :"))
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
        
savings = 0

# Monthly calculations
monthly_salary = annual_salary / 12
original_monthly_salary = monthly_salary

# loop for 36 months with 100% savings
for months in range(1, 37):
    savings += savings * monthly_return
    savings += monthly_salary
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_rise
if savings < Down_payment:
    print("It is not possible to pay the down payment in three years.")
    exit()
else:
    savings = 0

# initialising required variables
low_rate = 0
high_rate = 10000
mid_rate = (low_rate + high_rate) // 2
steps = 0

while True:
    # loop runs until we find required savings rate
    
    mid_rate = (low_rate + high_rate) // 2  
    # Find midpoint of current rate range
    
    rate = mid_rate / 10000             # convert midpoint into decimal savings rate

    savings = 0
    
    monthly_salary = original_monthly_salary        
    
    for months in range(1, 37):               
        # loop runs until 36 months completed. 
        savings += savings * monthly_return              # add monthly investment return
        savings += monthly_salary * rate                 # adds monthly savings
        if months % 6 == 0:
            # checks 6 months completed or not
            monthly_salary += monthly_salary * semi_annual_rise   
    steps += 1           # increases one step for each iteration.
    if abs(savings - Down_payment) <= 100:
        print(f'Best savings rate: {rate:.4f}')
        print(f'Steps in bisection search: {steps}')
        break
    elif high_rate - low_rate <= 1:
        
        print("It is not possible to find a suitable savings rate.")
        break

    elif savings < Down_payment:
        low_rate = mid_rate                # savings too low -> increase rate
        
    else:
        high_rate = mid_rate               # savings too high → decrease rate