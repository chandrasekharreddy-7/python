''' Create a function reduce to remove k characters so that each character appears
equally.
Example
check('aabbcc',0) -> 'aabbcc'
check('aabbbcc',0) -> ''
check('aabbbcc',1) -> 'aabbcc'
check('aabbbcc',4) -> 'abc'
check('aabbbcc',6) -> 'a' '''
def reduce(s, k):
    unique = ""
    for ch in s:
        if ch not in unique:
            unique += ch
    maxf = 0
    for ch in unique:
        count = s.count(ch)
        if count > maxf:
            maxf = count
    for f in range(maxf, -1, -1):
        remove = 0
        for ch in unique:
            c = s.count(ch)
            if c > f:
                remove += c - f
            else:
                remove += c
        if remove == k:
            result = ""
            for ch in unique:
                c = s.count(ch)
                keep = f if c >= f else 0
                result += ch * keep
            return result
    return ""
print(reduce('aabbcc',0))
print(reduce('aabbbcc',0))
print(reduce('aabbbcc',1))
print(reduce('aabbbcc',4))
print(reduce('aabbbcc',6))