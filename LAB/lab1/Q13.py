def extractdup(lst):
    result = []
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count = count + 1
        if count > 1 and lst[i] not in result:
            result.append(lst[i])
    return result
l = [10,20,30,20,30,40]
print(extractdup(l))