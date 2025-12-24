s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

def lengthOfLongestSubstring(s: str) -> int:
    # Time O(n) Space O(n)
    longest = 0
    sett = set()
    l = 0
    n = len(s)
    
    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        w = (r - l) + 1
        longest = max(longest,w)
        sett.add(s[r])
    return longest

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))


