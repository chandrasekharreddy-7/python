''' Write a program that takes a date in the format DDMMYYYY and prints the day of the week it
falls on. Given: 01-01-1990 was a Monday. '''
datemonthyear = input("enter date in ddmmyyyy format :")
date = int(datemonthyear[0:2])
month = int(datemonthyear[2:4])
year = int(datemonthyear[4:8])
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
total_days = 0
for i in range(1,year):
        if i % 4 == 0 and i % 100 != 0:
                total_days += 366
        elif i % 400 == 0:
                total_days += 366
        else:
                total_days += 365
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
for i in range(0,month-1):
        total_days += days_in_month[i]
total_days += date
day_number = total_days % 7
if day_number == 0:
        print("Sunday")
elif day_number == 1:
        print("Monday")
elif day_number == 2:
        print("Tuesday")
elif day_number == 3:
        print("Wednesday")
elif day_number == 4:
        print("Thursday")
elif day_number == 5:
        print("Friday")
elif day_number == 6:
        print("Saturday")


''' process - 2 '''
def find_day(datemonthyear):
    date = int(datemonthyear[0:2])
    month = int(datemonthyear[2:4])
    year = int(datemonthyear[4:8])
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    total_days = 0
    for i in range(1, year):
        if i % 4 == 0 and i % 100 != 0:
            total_days += 366
        elif i % 400 == 0:
            total_days += 366
        else:
            total_days += 365
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    for i in range(0, month - 1):
        total_days += days_in_month[i]
    total_days += date
    day_number = total_days % 7
    if day_number == 0:
        return "Sunday"
    elif day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
datemonthyear = input("Enter date in ddmmyyyy format: ")
print(find_day(datemonthyear))