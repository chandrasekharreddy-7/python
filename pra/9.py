''' Duplicate Character Management:
    Create a function moveDups that moves duplicate characters to the end of the
    string with an underscore (e.g., 'cartoon' -> 'carton_o'). '''
def dup_mover(string):
    new_str = ""
    dup = ""
    for i in string:
        if i not in new_str:
            new_str += i
        else:
            dup += i
    c_str = new_str + '_' + dup
    return c_str
string = input("enter a string :")
print(dup_mover(string))