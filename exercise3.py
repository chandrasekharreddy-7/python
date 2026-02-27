''' Write a program to count the number of vowels in a given string. '''
''' process - 1 '''
# string = input("enter a string :")
# vowels = "AEIOUaeiou"
# count = 0
# for i in string:
#     if i in vowels:
#         count+=1
# print(f"total number of vowels = {count}")

''' process - 2 '''
# string = input("enter a string :")
# count = 0
# for i in string:
#     if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" \
#         or i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         count+=1
# print(f"no of vowels = {count}")


''' Given a string, print all characters at even indices using a for loop. '''
''' process - 1 '''
# string = input("enter string :")
# count = 0
# for i in string:
#     count+=1
# for i in range(count):
#     if i % 2 == 0:
#         continue
#     else:
#         print(string[i])

''' process - 2 '''
# string = input("enter string :")
# length = len(string)
# for i in range(0,length):
#     if i % 2 == 0:
#         continue
#     else:
#         print(string[i])


''' Write a program to count how many uppercase and lowercase letters are present in a string. '''
# string = input("enter a string :")
# upper = 0
# lower = 0
# for i in string:
#     if ord(i) >= 65 and ord(i) <= 90:
#         upper+=1
#     elif ord(i) >= 97 and ord(i) <= 127:
#         lower+=1
#     else:
#         continue
# print(f"no of upper case letters = {upper}")
# print(f"no of lower case letters = {lower}")

''' process - 2 '''
# string = input("enter a string :")
# upper = 0
# lower = 0
# for i in string:
#     if i >= "a" and i <= "z":
#         lower+=1
#     elif i >= "A" and i <= "Z":
#         upper+=1
#     else:
#         continue
# print(f"no of upper case letters = {upper}")
# print(f"no of lower case letters = {lower}")


''' Given a string, print each character and check whether it is a vowel or a consonant. '''
# string = input("enter a string :")
# vowel = "AEIOUaeiou"
# for i in string:
#     if i in vowel:
#         print(f"{i} : vowel")
#     elif i >= "0" and i <= "9":
#         continue
#     else:
#         print(f"{i} : consonant")


''' Write a program to count the number of digits in a given string. '''
''' process - 1 '''
# string = input("enter a string :")
# count = 0
# for i in string:
#     if i >= "0" and i <= "9":
#         count+=1
#     else:
#         continue
# print(f"total number of digits in string = {count}")

''' process - 2 '''
# string = input("enter the string :")
# count = 0
# digits = "0123456789"
# for i in string:
#     if i in digits:
#         count+=1
# print(f"total number of digits in string = {count}")


''' Given a string, replace all vowels with the character * and print the modified string. '''
''' process - 1 '''
# string = input("enter a string :")
# string_list = list(string)     # strings are immutable
# vowels = "AEIOUaeiou"
# for i in range(len(string_list)):
#     if string_list[i] in vowels:
#         string_list[i] = '*'
# string = "".join(string_list)
# print(string)

''' process - 2 '''
# string = input("enter a string :")
# vowels = "AEIOUaeiou"
# character = "*"
# for vowel in vowels:
#     string = string.replace(vowel,character)
# print(string)


''' Write a program to check whether a string contains more vowels or more consonants. '''
# string = input("enter a string :")
# vowel = "AEIOUaeiou"
# vowel_count = 0
# consonant = 0
# for i in string:
#     if i in vowel:
#         vowel_count+=1
#     elif i >= "0" and i <= "9":
#         continue
#     elif i == " ":
#         continue
#     else:
#         consonant+=1
# if vowel_count > consonant:
#     print("in the given string, vowels are more")
# elif vowel_count == consonant:
#     print("in the given string, vowels and consonants are equal")
# else:
#     print("in the given string, consonants are more")

''' Given a string, print only those characters which are alphabets. '''
# string = input("enter a string :")
# for i in string:
#     if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
#         print(i,end = "")


''' Write a program to reverse a string using a for loop. '''
# string = input("enter the string :")
# length = len(string) - 1
# for i in range(length,-1,-1):
#     print(string[i],end = "")

''' without using for loop '''
# string = input("enter the string :")
# print(string[::-1])


''' Given a string, count the number of special characters (characters other than alphabets and digits). '''
# string = input("enter a string :")
# count = 0
# for i in string:
    # if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
    #     continue
    # elif i >= "0" and i <= "9":
    #     continue
    # else:
    #     count+=1
    #     print(i,end = "")
# print(f"no of special characters = {count}")


''' Write a program to count the number of vowels in a string using a while loop. '''
''' process - 1 '''
# string = input("enter a string :")
# i = 0
# vowels = "AEIOUaeiou"
# vowel = 0
# count = 0
# for a in string:
#     count+=1
# while i < count:
#     if string[i] in vowels:
#         vowel+=1
#     i+=1
# print(f"no of vowels = {vowel}")

''' process - 2 '''
# string = input("enter a string :")
# i = 0
# count = 0
# length = len(string)
# while i != length:
#     if string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U" \
#         or string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
#         count+=1
#     i+=1
# print(f"no of vowels = {count}")


''' Given a string, print all characters until a vowel is encountered using a while loop. '''
# string = input("enter a string :")
# i = 0
# count = 0
# length = len(string)
# while i < length:
#     if string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U" \
#         or string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
#         break
#     else:
#         print(string[i],end = "")
#     i+=1


''' write a program to count no of spaces in a given string. '''
# string = input("enter a string :")
# count = 0
# for i in string:
#     if i == " ":
#         count+=1
# if count > 0:
#     print("no of spaces = ",count)
# else:
#     print("there are no spaces in the given string")


''' given a string, print each character and check weather it is a digit or not '''
# string = input("enter a string :")
# for i in string:
#         if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
#             print(f"{i} : Alphabet")
#         elif i >= "0" and i <= "9":
#             print(f"{i} : Digit")
#         else:
#             print(f"{i} :Special Character")


''' write a program to find the first upper case letter in a string using while loop '''
# string = input("enter a string")
# length = len(string)
# i = 0
# while i < length:
#     if string[i] >= "A" and string[i] <= "Z":
#         print(f"the first uppercase letter in {string} : {string[i]}")
#     i+=1


''' given a string, count how many charcters are not alphabets. '''
# string = input("enter a string :")
# count = 0
# for i in string:
#     if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
#         continue
#     else:
#         count+=1
# print(f"no of characters other than alphabets = {count}")


''' Given a string, check whether the string contains at least one vowel. '''
# string = input("enter a string :")
# i = 0
# vowels = "AEIOUaeiou"
# vowel = 0
# count = 0
# for a in string:
#     count+=1
# while i < count:
#     if string[i] in vowels:
#         vowel+=1
#     i+=1
# if vowel > 0:
#     print("the string has atleast one vowel.")
# else:
#     print("the string has no vowels.")


''' Write a program to count the number of words in a string (words separated by spaces). '''
# string = input("enter a string :")
# count = 0
# for i in string:
#     if i == " ":
#         count+=1
#     else:
#         continue
# print(f"total no of words = {count+1}")


''' Given a string, print each character and classify it as vowel, consonant, digit, or special character. '''
# string = input("enter a string :")
# vowels = "AEIOUaeiou"
# for i in string:
#     if i in vowels:
#         print(f"{i} : vowel")
#     elif i >= "0" and i <= "9":
#         print(f"{i} : digit")
#     elif (i >= "A" and i <= "Z") or i >= "a" and i <= "z":
#         print(f"{i} : consonant")
#     else:
#         print(f"{i} : special character")


''' Write a program to print characters of a string in reverse order using a while loop. '''
# string = input("enter a string :")
# index = len(string) - 1
# print("reversed string = ",end = "")
# while index >= 0:
#     print(f"{string[index]}",end = "")
#     index-=1