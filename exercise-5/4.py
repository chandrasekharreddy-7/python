''' Create a function evenIndexCapital. Capitalize characters at even indices. Raise
UpperCaseException if input contains uppercase letters.
Example
evenIndexCapital('school') -> 'ScHoOl' '''
def evenIndexCapital(string):
    result = ""
    for i in range(len(string)):
        if 'A' <= string[i] <= 'Z':
            result += string[i]
        elif i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i]
    return result
print(evenIndexCapital("chandra"))