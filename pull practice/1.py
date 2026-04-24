def is_palindrome(s : str) -> bool:
    s1 = s.lower()
    new_str = ""
    for i in s1:
        if i.isalpha():
            new_str += i
    if new_str == new_str[::-1]:
        return True
    return False
print(is_palindrome("A man, a plan, a canal: Panama"))