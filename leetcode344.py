s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]

def reverseString(s: list[str]) -> list[str]:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

print(reverseString(s1))        
print(reverseString(s2))        