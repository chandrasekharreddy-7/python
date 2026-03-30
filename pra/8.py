''' Character Extraction:
    Create a function firstLetters that returns the first letter of every 
    word in a sentence (e.g., 'bad is nice' -> 'bin'). '''
def char_extraction(string):
    c = string[0]
    for i in range(len(string)):
        if string[i] == " ":
            c += string[i+1]
    return c
string = input("enter a string :")
c = char_extraction(string)
print(c)