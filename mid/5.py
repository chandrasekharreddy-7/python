''' Create a function delVowels that removes all vowels.
Example
delVowels('SfgEtfjofubjiekp') -> 'Sfgtfjfbjkp'
delVowels('aEiOu'') -> '' '''
def del_vowels(string):
    vowels = "aeiouAEIOU"
    new_str = ""
    for i in string:
        if i not in vowels:
            new_str += i
    return new_str
print(del_vowels('SfgEtfjofubjiekp'))
print(del_vowels('aEiOu'))