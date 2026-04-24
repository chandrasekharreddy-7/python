#method 1 : using sorting
def is_anagram(s: str, t: str) -> bool:
    if sorted(s) == sorted(t):
        return True
    return False
print(is_anagram("rat", "car"))

#method 2 : Count frequency of each character using dictionary
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True
print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))          
print(is_anagram("listen", "silent"))