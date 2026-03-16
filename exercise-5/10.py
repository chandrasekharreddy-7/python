''' Create a function separate that groups identical characters.
Example
separate('cartoon') -> ['c','a','r','t','oo','n']
separate('network') -> ['n','e','t','w','o','r','k']
separate('aabbcc') -> ['aa','bb','cc']
separate('cccbbaaa') -> ['ccc','bb','aaa'] '''
def separate(string):
    result = []
    group = string[0]
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            group += string[i]
        else:
            result.append(group)
            group = string[i]
    result.append(group)
    return result
print(separate('cartoon'))
print(separate('network'))
print(separate('aabbcc'))
print(separate('cccbbaaa'))