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