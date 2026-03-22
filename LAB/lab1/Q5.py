def checkpalindrome(s):
    length = 0
    for char in s: length += 1 # Manual length count
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return "Not a Palindrome"
    return "palindrome"
string = input("enter a string :")
print(checkpalindrome(string))