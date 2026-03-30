''' Create a function minIndexFirstString that takes two strings str1 and str2. Return
the largest index of a character in str1 that is also present in str2. If none exist return
-1.
Example
minIndexFirstString('tiger','integer') -> 4
minIndexFirstString('integer','tiger') -> 6 '''
def minindexfirststring(s1, s2):
    max_index = -1
    for i in range(len(s1)):
        if s1[i] in s2:
            max_index = i
    return max_index
print(minindexfirststring('tiger','integer'))
print(minindexfirststring('integer','tiger'))