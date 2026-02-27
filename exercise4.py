''' Write and test a function named check leap year that takes as parameter a year between 1600
and 9999. It should return True if the year is a leap year and False otherwise. '''
# def leapyearcheck(year):
#     if year > 1600 and year < 9999:
#         if year % 4 == 0 and year % 100 != 0:
#             return True
#         elif year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         print("please enter correct year between 1600 and 9999.")
#         return None
# year = int(input("enter a year (1600 - 9999) to check leap year or not :"))
# print(f"{leapyearcheck(year)}")


''' Write and test a function that takes a word as input and prints the number of vowels and
consonants in it. '''
# def vowelandconsonantcount(word):
#     vowels = "AEIOUaeiou"
#     vowel = 0
#     consonant = 0
#     for i in word:
#         if i in vowels:
#             vowel+=1
#         elif ("a" <= i <= "z") or ("A" < i <= "Z"):
#             consonant+=1
#         else:
#             continue
#     return vowel, consonant
# word = input("enter a word :")
# print(f"(vowels, consonants) = {vowelandconsonantcount(word)}")


''' Write and test a function that takes a number as parameter and prints the multiplication table
of that number. '''
# def multiplicationtable(n):
#     print(f"*****   MULTIPLICATION TABLE OF {n}   *****")
#     for i in range(1,11):
#         mult = 0
#         mult = n * i
#         print(f"{n} x {i} = {mult}")
# n = int(input("enter the number to print its multiplication table :"))
# multiplicationtable(n)


''' Write a function that takes three numbers as parameters and returns the median value of those
parameters. '''
# def medianof(x, y, z):
#     if (y < x and x < z) or (z < x and x < y):
#         median = x
#         return median
#     elif (x < y and y < z) or (z < y and y < x):
#         median = y
#         return median
#     else:
#         median = z
#     return median
# x = int(input("enter 1st integer :"))
# y = int(input("enter 2nd integer :"))
# z = int(input("enter 3rd integer :"))
# print(f"median = {medianof(x, y, z)}")


''' Write and test a function add square that returns the square of its parameter. '''
# def add_square(n):
#     if n == 0:
#         return 0
#     else:
#         return n * n
# a = int(input("enter an integer to print its square :"))
# print(f"square of {a} = {add_square(a)}")


''' Write a function called calcSeconds() which takes three arguments for hours, minutes, and
seconds and returns the total time in seconds. Example: calcSeconds(1, 3, 20) should
return 3800. '''
# def calcseconds(hours, minutes, seconds):
#     total_seconds = 0
#     hour_seconds = hours * 60 * 60
#     minute_seconds = minutes * 60
#     total_seconds = hour_seconds + minute_seconds + seconds
#     return total_seconds
# hours = int(input("enter no of hours :"))
# minutes = int(input("enter no of minutes :"))
# seconds = int(input("enter no of seconds :"))
# print(f"total no of seconds = {calcseconds(hours, minutes, seconds)}")


''' Write a function named IIT() that takes a character as an argument and prints IIT in that
character. Example:
Input: '.'
Output:
.
.
.
.
.
.
.
.
. . . . .
.
.
. '''
# def IIT(ch):
#     for i in range(5):
#         print(ch, end="   ")
#         print(ch, end="   ")
#         if i == 0:
#             print(ch * 5, end="")
#         else:
#             print("  " + ch + "  ", end="")
#         print()
# IIT('.')


''' Write a function add square() that takes a 3-digit integer as its argument and finds the sum
of the squares of digits in the number. '''
# def add_square(num):
    # count = 0
    # o_num = num
    # x_num = num
    # while o_num > 0:
    #     rem = o_num % 10 
    #     count+=1
    #     o_num //= 10
    # if count == 3:
    #     sum = 0
    #     while num > 0:
    #         r = num % 10
    #         sum += r ** 2
    #         num //= 10
    #     print(f"sum of squares of digits in {x_num} = {sum}")
    # else:
    #     print("please enter a three digit - integer")
    # pass
# num = int(input("enter a three digit integer :"))
# add_square(num)


''' Write a function that takes a 3-digit positive integer as its argument and reverses it. Example:
Input: 123, Output: 321 Input: 120, Output: 21 '''
# def reverse(num):
#     count = 0
#     o_num = num
#     x_num = num
#     while o_num > 0:
#         rem = o_num % 10 
#         count+=1
#         o_num //= 10
#     if count == 3:
#         rev = 0
#         while num > 0:
#             r = num % 10
#             rev = rev * 10 + r
#             num //= 10
#         print(f"reverse of {x_num} = {rev}")
#     else:
#         print("please enter a three digit - integer")
#     pass
# num = int(input("enter a three digit integer :"))
# reverse(num)


''' Write a function that takes as an argument a parameter of type Point and returns True if it
lies within the square connecting the points (0, 0), (1, 0), (0, 1), (1, 1); and False otherwise. '''
# def is_inside_square(point):
#     x, y = point
#     if 0 <= x <= 1 and 0 <= y <= 1:
#         return True
#     else:
#         return False
# p1 = x, y = float(input("enter x - coordinate of the point :")), float(input("enter y - coordinate of the point :"))
# print(f"{is_inside_square(p1)}")


''' Write a Python function called quadratic roots that takes three arguments (a, b, c) represent-
ing the coefficients of a quadratic equation ax2 + bx + c = 0. The function should return the
positive real root if one exists; otherwise, return None. '''
# def quadratic_roots(a, b, c):
#     d = 0
#     d = (b** 2)- (4*a*c)
#     if d >= 0:
#         root1,root2 = (-b + d**1/2)/2*a , (-b - d**1/2)/2*a
#         if root1 > 0:
#             return root1
#         elif root2 > 0:
#             return root2
#         else:
#             return None
#     else:
#         return None
# a,b,c = float(input("enter co-efficient of x^2 :")), float(input("enter co-efficient of x :")), float(input("enter constant value :"))
# print(f"{quadratic_roots(a,b,c)}")


''' Write a function cubesum that accepts a 3-digit integer and returns the sum of the cubes of
individual digits of that number. Use this function in another function isArmstrong to check
if its 3-digit parameter is an Armstrong number. Example: 371 is an Armstrong number since
3^3 + 7^3 + 1^3 = 371. '''
# def amstrong_number_check(org_number):
#     number = org_number
#     total_sum = 0
#     while number > 0:
#         rem = number % 10
#         total_sum += rem**3
#         number //= 10
#     if total_sum == org_number:
#         return True
#     else:
#         return False
# num = int(input("enter a 3-digit integer number to check it is a amstrong number or not :"))
# print(f"{amstrong_number_check(num)}")


''' Write a function prodDigits that takes a 5-digit number as its parameter and returns the
product of the digits of the number. '''
# def prodDigits(num):
#     org_num = num
#     pro = 1
#     count = 0
#     while num > 0:
#         rem = num % 10
#         pro *= rem
#         num //= 10
#         count+=1
#     if count == 5:
#         print(f"products of digits in {org_num} = {pro}")
#     else:
#         print("please enter a 5-digit number.")
# num = int(input("enter a 5-digit number :"))
# prodDigits(num)


''' Write a function that returns the non-negative square root of a number rounded to the nearest
integer. '''
# def round_square_root(num):
#     if num < 0:
#         print("enter a non-neagtive number to find square root.")
#     else:
#         sqrt_num = num**0.5
#         sqrt_num = sqrt_num//1
#         print(f"square root of {num} = {sqrt_num}")
# num = int(input("enter a non-negative number to find square root :"))
# round_square_root(num)

''' Note: Students are expected to write clean, well-documented Python code and test each function
with multiple inputs. '''