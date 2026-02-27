''' Q10 . Write a program that takes a year as input and prints whether it is a leap year or not.
        Note: The year can be any year in the past or up to 100 years into the future. '''
''' process - 1 '''
year = input("Enter a year (to check leap year or not): ")
if year.isdigit():
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year.")
    elif year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Please enter a valid year.")


''' process - 2 '''
def leapyearcheck(year):
    if year.isdigit():
        year = int(year)
        if year % 4 == 0 and year % 100 != 0:
            print(f"{year} is a leap year.")
        elif year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("please enter a valid year.")
year = input("enter a year (to check leap year or not) :")
leapyearcheck(year)