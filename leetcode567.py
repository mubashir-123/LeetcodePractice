s1 = "ab"
s2 = "eidbaooo"
s3 = "ab"
s4 = "eidboaoo"
s5 = "ab"
s6 = "a"

def checkInclusion(s1: str, s2: str) -> bool:
    # Time O(n) Space O(1)
    n1 = len(s1)
    n2 = len(s2)

    if n1 > n2:
        return False
    
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(n1):
        c1[ord(s1[i]) - 97] += 1
        c2[ord(s2[i]) - 97] += 1
    
    if c1 == c2:
        return True
    
    for i in range(n1,n2):
        c2[ord(s2[i]) - 97] += 1
        c2[ord(s2[i - n1]) - 97] -= 1

        if c1 == c2:
            return True
    return False

print(checkInclusion(s1,s2))
print(checkInclusion(s3,s4))
print(checkInclusion(s5,s6))
