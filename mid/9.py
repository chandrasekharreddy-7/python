''' Create a function fee that calculates the total fee paid until the academic year 2022 -
23.
Example
fee(100000,'CS20143') -> 331000
fee(100000,'DS18243') -> 210000
fee(100000,'EE16243') -> InvalidRollException '''
def fee(amount, rollno):
    year = rollno[2:4]
    year = int(year)
    if year < 18:
        return "InvalidRollException"
    r = 23 - year
    total = 0
    for i in range(r):
        total += amount
        amount *= 1.1
    return total
print(fee(100000,'CS20143'))
print(fee(100000,'DS18243'))
print(fee(100000,'EE16243'))
