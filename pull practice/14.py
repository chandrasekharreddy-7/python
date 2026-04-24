def group_anagrams(strs: list) -> list:
    groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    return list(groups.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
print(group_anagrams(["abc", "bca", "cba", "def", "fed"]))