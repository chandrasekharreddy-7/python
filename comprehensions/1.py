t = (3, 1, 4, 2, 42, 52, 14)
l = list(t)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j] <= l[i]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
t1 = tuple(l)
print(t1)