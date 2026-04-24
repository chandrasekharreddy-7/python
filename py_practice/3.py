def length_of_longest_substring(s: str) -> int:
    max_length = 0
    for i in range(len(s)):
        current = ""
        for j in range(i, len(s)):
            if s[j] in current:
                break
            current = current + s[j]
            if len(current) > max_length:
                max_length = len(current)
    return max_length
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
print(length_of_longest_substring("dvdf"))      # 3
