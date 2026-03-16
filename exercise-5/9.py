''' Create a function moveDups that moves duplicate characters to the end with ' '.
Example
moveDups('cartoon') -> 'carton_o'
moveDups('network') -> 'network'
moveDups('aabbcc') -> 'abc_abc'
moveDups('cccbbaaa') -> 'cba_ccbaa' '''
def movedups(string):
    org = ""
    dup = ""
    for i in string:
        if i not in org:
            org += i
        else:
            dup += i
    if dup == "":
        return f"'{string}' has no duplicate charcaters"
    else:
        return f"'{org+'_'+dup}'"
print(movedups('cartoon'))
print(movedups('network'))
print(movedups('aabbcc'))
print(movedups('cccbbaaa'))