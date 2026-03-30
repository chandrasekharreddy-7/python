''' Leap Year Validation: 
    Write a function check_leap_year that takes a year between 1600 and 9999 and 
    returns True if it is a leap year and False otherwise. '''
def check_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
year = int(input("enter year to chexk leap year or not :"))
print(check_leap_year(year))