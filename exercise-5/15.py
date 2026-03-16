''' Create a function subPali that returns the length of the longest palindromic substring.
Example
subPali('bbbabcbabdfb') -> 7
subPali('abcdefg') -> 1 '''
def subPali(s):
    n = len(s)
    max_len = 1
    for i in range(n):
        for j in range(i, n):
            left = i
            right = j
            flag = 1
            while left < right:
                if s[left] != s[right]:
                    flag = 0
                    break
                left = left + 1
                right = right - 1
            if flag == 1:
                length = j - i + 1
                if length > max_len:
                    max_len = length
    return f"length of the longest palindromic substring ({s}) = {max_len}"
print(subPali('bbbabcbabdfb'))
print(subPali('abcdefg'))