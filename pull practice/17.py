def first_uniq_char(s: str) -> int:
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1
print(first_uniq_char("leetcode"))      # 0
print(first_uniq_char("loveleetcode"))  # 2
print(first_uniq_char("aabb"))          # -1
print(first_uniq_char("abcabc"))        # -1