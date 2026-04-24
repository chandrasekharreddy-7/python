from itertools import groupby
def compress(chars: list) -> int:
    result = []
    for char, group in groupby(chars):
        count = len(list(group))
        result.append(char)
        if count > 1:
            result.extend(str(count))
    chars[:] = result
    return len(chars)

chars1 = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars1))
print(chars1)

chars2 = ["a"]
print(compress(chars2))
print(chars2)

chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(chars3))
print(chars3)

chars4 = ["a", "a", "a"]
print(compress(chars4))
print(chars4)