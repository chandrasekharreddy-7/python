# l = [2,1,3,4,5,1]
def longest_subsequent(l):
    res = []
    for i in range(len(l)):
        s = 1
        ind = i
        for j in range(i+1,len(l)):
            if l[i] < l[j]:
                s += 1
            else:
                break
        res.append(s)
    return f"longest subsequent = {max(res)}"
l = [5,1,3,0,6,7]
print(longest_subsequent(l))