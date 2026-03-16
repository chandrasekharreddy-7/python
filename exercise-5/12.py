''' Create a function fee that calculates the total fee paid until the academic year 2022–
23.
Example
fee(100000,'CS20143') -> 331000
fee(100000,'DS18243') -> 210000
fee(100000,'EE16243') -> InvalidRollException '''
def fee(amount, roll):
    year = int(roll[2:4])
    if year < 18:
        return "InvalidRollException"
    years = 23 - year
    total = 0
    for i in range(years):
        total += int(amount)
        amount = amount * 1.1
    return int(total)
print(fee(100000,'CS20143'))
print(fee(100000,'DS18243'))
print(fee(100000,'EE16243'))