ransomNote1 = "a"
magazine1 = "b"
ransomNote2 = "aa"
magazine2 = "ab"
ransomNote3 = "aa"
magazine3 = "aab"

def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter = {}

    for c in magazine:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for c in ransomNote:
        if c not in counter:
            return False
        elif counter[c] == 1:
            del counter[c]
        else:
            counter[c] -= 1
    return True

print(canConstruct(ransomNote1,magazine1))            
print(canConstruct(ransomNote2,magazine2))            
print(canConstruct(ransomNote3,magazine3))            

# Time O(m + n) 
# Space O(1)