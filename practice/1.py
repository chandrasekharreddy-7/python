def target_sum(l,s):
    length = len(l)
    count = 0
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if l[i] + l[j] + l[k] == s:
                    count+=1
    return f"total no of combinations = {count}"
l = []
length = int(input("enter length of the list :"))
for i in range(length):
    x = input(f"enter element {i + 1} :")
    l.append(x)
s = int(input("enter the target sum :"))
print(target_sum(l,s))