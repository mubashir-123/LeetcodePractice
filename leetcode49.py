from collections import defaultdict
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

def anagramGroup(strs: list[list[str]]) -> list[list[str]]:
    # Time O(n * m) Space O(n * m)
    anagram_dict = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)
        anagram_dict[key].append(s)

    return list(anagram_dict.values())        

print(anagramGroup(strs1))
print(anagramGroup(strs2))
print(anagramGroup(strs3))