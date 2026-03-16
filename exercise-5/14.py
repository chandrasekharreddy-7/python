''' Create a function equivalent to find the longest substring rotationally equivalent.
Example
equivalent('hdjkoul','pokoudj') -> 'djkou'
equivalent('ghajiop','abkoidj') -> 'io'
equivalent('hdjkoul','pikpiaa') -> '' '''
def equivalent(str1, str2):
    n = len(str1)
    for length in range(n, 0, -1):
        for i in range(n - length + 1):
            sub = ""
            j = i
            while j < i + length:
                sub = sub + str1[j]
                j = j + 1
            m = len(sub)
            k = 0
            while k < m:
                rotation = ""
                a = k
                while a < m:
                    rotation = rotation + sub[a]
                    a = a + 1
                b = 0
                while b < k:
                    rotation = rotation + sub[b]
                    b = b + 1
                if rotation in str2:
                    return sub
                k = k + 1
    return ""
print(equivalent('hdjkoul','pokoudj'))
print(equivalent('ghajiop','abkoidj'))
print(equivalent('hdjkoul','pikpiaa'))