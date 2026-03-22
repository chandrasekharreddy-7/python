def merge_the_tools(s, k):
    l = len(s)
    if l % k != 0:
        return "please enter correct string."
    new_l = []
    temp = ""
    for i in range(l):
        temp += s[i]
        if (i + 1) % k == 0:
            new_l.append(temp)
            temp = ""
    for i in range(len(new_l)):
        x = new_l[i]
        temp = ""
        for j in range(k):
            if x[j] not in temp:
                temp += x[j]
        print(temp)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)