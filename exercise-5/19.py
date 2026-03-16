''' Create a function weave that interweaves two equal-length lists.
Example
weave([],[]) -> []
weave([1,2,3],[4,5,6]) -> [1,2,3,4,5,6] '''
def weave(l , m):
    len1 = len(l)
    len2 = len(m)
    if len1 == len2 :
        for i in range(len1):
            l.append(m[i])
        return f"list after weaving : {l}"
    else:
        return f"enter equal length of strings."
print(weave([],[]))
print(weave([1,2,3],[4,5,6]))
print(weave([1,2,'chandra'],[3,4,'sekhar']))