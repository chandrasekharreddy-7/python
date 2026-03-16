''' Create a function delDup that removes duplicates.
Example
delDup([10,20,30,20,20,30,40,50,-20,60,60,-20,-20])
-> [10,20,30,40,50,-20,60]
delDup([-1,1,-1,8]) -> [-1,1,8] '''
def deldup(l):
    d = []
    for i in range(len(l)):
        if l[i] not in d:
            d.append(l[i])
    return f"list after deleting duplicate elements : {d}"
l = []
length = int(input("enter length of the list :"))
for i in range(length):
    x = input(f"enter element {i + 1} :")
    l.append(x)
print(f"{deldup(l)}")