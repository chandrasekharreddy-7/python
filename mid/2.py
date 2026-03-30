''' Create a function evenIndexCapital. Capitalize characters at even indices. Raise
UpperCaseException if input contains uppercase letters.
Example
evenIndexCapital('school') -> 'ScHoOl' '''
def evenindexcapital(string):
    new_str = ""
    for i in range(len(string)):
        if i % 2 == 0:
            if 'a' <= string[i] <= 'z':
                x = chr(ord(string[i]) ^ 32)
                new_str += x
        else:
            new_str += string[i]
    return new_str
print(evenindexcapital("school"))