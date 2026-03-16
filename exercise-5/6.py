''' Create a function distChar that returns sorted characters not common in the two
strings.
Example
distChar('characters','alphabets') -> 'bclpr'
distChar('apples','oranges') ->''glnopr'
distChar('apples','apples') -> '' '''
def distChar(str1, str2):
    new_str = ""
    for ch in str1:
        if ch not in str2 and ch not in new_str:
            new_str += ch
    for ch in str2:
        if ch not in str1 and ch not in new_str:
            new_str += ch
    new_str = sorted(new_str)
    result = ""
    for ch in new_str:
        result += ch
    if result != "":
        return result
    else:
        return "' '"
print(distChar('characters','alphabets'))
print(distChar('apples','oranges'))
print(distChar('apples','apples'))