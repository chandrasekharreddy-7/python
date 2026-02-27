''' Q8 : Write a program that takes a 4-letter word as input and toggles the case of all its letters
using bitwise operations. Example: Input: HeLLo
Output: hEllO '''
''' process - 1 ''' 
word = input("enter a 4 letter word :")
if len(word) == 4:
    toggled_word = ""
    for ch in word:
        toggled_ch = chr(ord(ch) ^ 32)
        toggled_word += toggled_ch
    print(f"Toggled case: {toggled_word}")


''' process - 2 '''
def toggle_case(word):
    if len(word) == 4:
        toggled_word = ""
        for ch in word:
            toggled_ch = chr(ord(ch) ^ 32)
            toggled_word += toggled_ch
        return f"Toggled case: {toggled_word}"
    else:
        return "Please enter a 4-letter word."
word = input("Enter a 4 letter word: ")
print(toggle_case(word))