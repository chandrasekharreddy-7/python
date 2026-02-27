''' Q20 : Write a program that takes a character as input and prints the alpha-numeric character (0–9,
A - Z, a - z are alpha-numeric characters) that is closest to this character.
Note: If the input character is equidistant from two alpha-numeric values, either one can
be printed. '''
ch = input("Enter a character: ")
if len(ch) != 1:
    print("Invalid input")
else:
    a = ord(ch)
    if ('0' <= ch <= '9') or ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        print("Closest alpha-numeric character:", ch)
    elif a < ord('0'):
        print("Closest alpha-numeric character: 0")
    elif ord('9') < a < ord('A'):
        if a - ord('9') < ord('A') - a:
            print("Closest alpha-numeric character: 9")
        else:
            print("Closest alpha-numeric character: A")
    elif ord('Z') < a < ord('a'):
        if a - ord('Z') < ord('a') - a:
            print("Closest alpha-numeric character: Z")
        else:
            print("Closest alpha-numeric character: a")
    else:
        print("Closest alpha-numeric character: z")


''' process - 3 '''
def closest_alphanumeric(ch):
    if len(ch) != 1:
        return "Invalid input"
    else:
        a = ord(ch)
        if ('0' <= ch <= '9') or ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            return f"Closest alpha-numeric character: {ch}"
        elif a < ord('0'):
            return "Closest alpha-numeric character: 0"
        elif ord('9') < a < ord('A'):
            if a - ord('9') < ord('A') - a:
                return "Closest alpha-numeric character: 9"
            else:
                return "Closest alpha-numeric character: A"
        elif ord('Z') < a < ord('a'):
            if a - ord('Z') < ord('a') - a:
                return "Closest alpha-numeric character: Z"
            else:
                return "Closest alpha-numeric character: a"
        else:
            return "Closest alpha-numeric character: z"
ch = input("Enter a character: ")
print(closest_alphanumeric(ch))