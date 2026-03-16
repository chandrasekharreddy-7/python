''' A palindrome is a word that reads the same backward as forwards.
Create a function checkPalindrome to check whether the string passed as its argument
is a palindrome.
Example
checkPalindrome('madam') -> True
checkPalindrome('racecar') -> True
checkPalindrome('python') -> False '''
''' process - 1 (using slicing) '''
def checkpalindrome(string):
    if string.isalpha():
        if string != string[::-1]:
            return f"False"
        else:
            return f"True"
    else:
        return f"please enter a word string."
print(checkpalindrome("madam"))
print(checkpalindrome("racecar"))
print(checkpalindrome("python"))


''' process - 2 '''
def checkpalindrome(string):
    if string.isalpha():
        length = len(string)
        rev_string = ""
        for i in range(length):
            rev_string = string[i] + rev_string
        if rev_string == string:
            return f"True"
        else:
            return f"False"
    else:
        return f"please enter a word string."
print(checkpalindrome("madam"))
print(checkpalindrome("racecar"))
print(checkpalindrome("python3"))