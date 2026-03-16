''' Create a function minOp to compute minimum edit operations between two strings.
Example
minOp('python','pythons') -> 1
minOp('abc','') -> 3
minOp('abc','def') -> 3
minOp('ab','def') -> 3 '''
def minop(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    count = 0
    if len1 >= len2:
        for i in str1:
            if i not in str2:
                count += 1
    else:
        for i in str2:
            if i not in str1:
                count += 1
    return f"total no of minimum edit operations = {count}"
print(minop('python','pythons'))
print(minop('abc',''))
print(minop('abc','def'))
print(minop('ab','def'))