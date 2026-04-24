def longest_palindrome(s: str) -> str:
    longest = ""
    for i in range(len(s)):
        # Case 1: odd length palindrome
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current = s[left:right + 1]
            if len(current) > len(longest):
                longest = current
            left -= 1
            right += 1
        # Case 2: even length palindrome
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current = s[left:right + 1]
            if len(current) > len(longest):
                longest = current
            left -= 1
            right += 1
    return longest
print(longest_palindrome("babad"))  # bab or aba
print(longest_palindrome("cbbd"))   # bb
print(longest_palindrome("a"))      # a
print(longest_palindrome("ac"))     # a or c