def kmax(l,k):
    if k <= 0 or k > len(l):
        return f"please enter correct value."
    temp = l[:]
    for _ in range(k):
        max_val = temp[0]
        for x in temp:
            if x > max_val:
                max_val = x
        temp.remove(max_val)
    return max_val
print(kmax([10, 2, 4, 5, 7, 9],2))