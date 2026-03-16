''' Create a function firstLetters that returns the first letter of every word.
Example
firstLetters('bad is nice') -> 'bin'
firstLetters('hello other world') -> 'how' '''
def firstletters(string):
    length = len(string)
    new_str = string[0]
    for i in range(length):
        if string[i] == " ":
            new_str += string[i+1]
    return f"first letters before each word in the string = {new_str}"
print(firstletters("bad is nice"))
print(firstletters("hello other world!"))