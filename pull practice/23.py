def find_anagrams(s: str, p: str) -> list:
    result = []
    p_sorted = sorted(p)
    length = len(p)
    for i in range(len(s) - length + 1):
        part = s[i:i + length]
        if sorted(part) == p_sorted:
            result.append(i)
    return result
print(find_anagrams("cbaebabacd", "abc"))  # [0, 6]
print(find_anagrams("abab", "ab"))         # [0, 1, 2]
print(find_anagrams("aaaaaaaa", "aa"))     # [0, 1, 2, 3, 4, 5, 6]
print(find_anagrams("hello", "ll"))        # [2]