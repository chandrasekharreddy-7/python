''' Palindrome Checker: 
    Create a function checkPalindrome to check whether a string passed as its 
    argument is a palindrome (e.g., 'madam' -> True). '''
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False
string = input("enter string :")
print(is_palindrome(string))