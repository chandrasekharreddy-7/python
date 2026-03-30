''' Minimum Edit Operations:
    Create a function minop to compute the minimum number of edit operations 
    (insertions, deletions, or substitutions) needed to change one string into another. '''
def minop(s1, s2):
    count = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            count += 1
    count += abs(len(s1) - len(s2))
    return count
s1 = input("enter first string: ")
s2 = input("enter second string: ")
print("minimum operations:", minop(s1, s2))