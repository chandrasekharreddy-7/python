''' Create a function extractDup that returns integers with duplicates.
Example
extractDup([10,20,30,20,20,30,40,50,-20,60,60,-20,-20]) -> [20,30,60,-20]
extractDup([-1,1,-1,8]) -> [-1]
extractDup([-3,1,-1,8]) -> [] '''
def extractDup(lst):
    result = []
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count = count + 1
        if count > 1 and lst[i] not in result:
            result.append(lst[i])
    return result
print(extractDup([10,20,30,20,20,30,40,50,-20,60,60,-20,-20]))
print(extractDup([-1,1,-1,8]))
print(extractDup([-3,1,-1,8]))