def delvowels(string):
    new_str = ""
    vowels = "AEIOUaeiou"
    for i in string:
        if i not in vowels:
            new_str += i
    if new_str != "":
        return new_str
    else:
        return "None"
print(delvowels("SfgEtfjofubjiekp"))