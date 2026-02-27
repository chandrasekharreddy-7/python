''' Q19 : Write a program that takes a 2-letter word as input and prints it in small letters.
Note: Each letter of the input word can be in capital or small letters. '''
word = input("enter a two letter word :")
length = len(word)
if length != 2:
    print("please enter a two - letter word.")
else:
    smallword = ""
    for i in word:
        if i >= 'a' and i <= 'z':
            smallword = smallword + i
        else:
            i = ord(i)
            i = i + 32
            i = chr(i)
            smallword = smallword + i
    print(smallword)

''' process - 2(using in built functions.) '''
word = input("enter a two letter word (to converet into lower case.)")
length = len(word)
if length == 2 and word.isalpha():
    small = word.lower()
    print(small)
else:
    print("please enter a two letter word.")


''' process - 3 '''
def convert_to_lower(word):
    if len(word) != 2:
        return "Please enter a two-letter word."
    else:
        smallword = ""
        for i in word:
            if 'a' <= i <= 'z':
                smallword += i
            else:
                i = chr(ord(i) + 32)
                smallword += i
        return smallword
word = input("Enter a two-letter word: ")
print(convert_to_lower(word))