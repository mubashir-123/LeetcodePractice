s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

def isAnagram(s: str, t:str) -> bool:
    s_counter = {}
    t_counter = {}

    if len(s) != len(t):
        return False

    for s_char, t_char in zip(s,t):
        s_counter[s_char] = s_counter.get(s_char,0) + 1
        t_counter[t_char] = t_counter.get(t_char,0) + 1

    return s_counter == t_counter    

print(isAnagram(s1,t1))
print(isAnagram(s2,t2))

# Time O(n) Space O(n)

