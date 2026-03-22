def distChar(str1, str2):
    new_str = ""
    for ch in str1:
        if ch not in str2 and ch not in new_str:
            new_str += ch
    for ch in str2:
        if ch not in str1 and ch not in new_str:
            new_str += ch
    new_str = sorted(new_str)
    result = ""
    for ch in new_str:
        result += ch
    if result != "":
        return result
    else:
        return "' '"
print(distChar('characters','alphabets'))