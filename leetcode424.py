s1 = "ABAB"
k1 = 2
s2 = "AABABBA"
k2 = 1

def characterReplacement(s: str,k: int) -> int:
    # Time O(n) Space O(1)
    longest = 0
    l = 0
    count = [0] * 26

    for r in range(len(s)):
        count[ord(s[r]) - 65] += 1
        while (r - l + 1) - max(count) > k:
            count[ord(s[l]) - 65] -= 1
            l += 1
        longest = max(longest,(r - l + 1))
    return longest

print(characterReplacement(s1,k1)) 
print(characterReplacement(s2,k2)) 