''' Create a function change that returns the minimum number of changes needed to
make all characters equal.
Example
change('R') -> 0
change('RGRGR') -> 2
change('GRG') -> 1 '''
def change(string):
    max_count = 0
    for ch in string:
        count = 0
        for c in string:
            if c == ch:
                count += 1
        if count > max_count:
            max_count = count
    return len(string) - max_count
print(change('R'))
print(change('RGRGR'))
print(change('GRG'))
print(change('AABAC'))