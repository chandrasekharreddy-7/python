def sub_string_count(s,s1):
    len1 = len(s)
    len2 = len(s1)
    dif = len1 - len2 
    l = []
    for i in range(dif + 1):
        temp = ""
        for j in range(len2):
            temp += s[i+j]
        l.append(temp)
    count = l.count(s1)
    return count
s = input("enter a string :")
s1 = input("enter substring :")
print(sub_string_count(s,s1))