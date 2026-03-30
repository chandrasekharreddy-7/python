''' Create a function distChar that returns sorted characters not common in the two
strings.
Example
distChar('characters','alphabets') -> 'bclpr'
distChar('apples','oranges') ->''glnopr'
distChar('apples','apples') -> '' '''
def distchar(s1,s2):
    new_str = ""
    for i in s1:
        if i not in s2 and i not in new_str:
            new_str += i
    for i in s2:
        if i not in s1 and i not in new_str:
            new_str += i
    return new_str
print(distchar('characters','alphabets'))
print(distchar('apples','oranges'))
print(distchar('apples','apples'))