''' Create a function moveDups that moves duplicate characters to the end with ' '.
Example
moveDups('cartoon') -> 'carton_o'
moveDups('network') -> 'network'
moveDups('aabbcc') -> 'abc_abc'
moveDups('cccbbaaa') -> 'cba_ccbaa' '''
def move_dups(string):
    new_str = ""
    new_str1 = ""
    for i in string:
        if i not in new_str:
            new_str += i
        else:
            new_str1 += i
    return new_str + '_' + new_str1
print(move_dups('cartoon'))
print(move_dups('network'))
print(move_dups('aabbcc'))
print(move_dups('cccbbaaa'))