s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

# Time O(n)
# Space(1)

def isPalindrome(s: str) -> bool:
    n = len(s)
    l = 0
    r = n - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))