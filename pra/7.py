''' String Rotation:
    Create a function shift that rotates a string left by acount and then right by ccount. '''
def string_rotation(string, acount, ccount):
    if acount >= len(string) or ccount >= len(string):
        return "acount and ccount must be less than length of given string."
    left_rotated = string[acount:] + string[:acount]
    right_rotated = string[-ccount:] + string[:-ccount]
    return left_rotated, right_rotated
string = input("enter a string: ")
left, right = string_rotation(string, 2, 3)
print("after left rotation:", left)
print("after right rotation:", right)