
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

def longestCommonPrefix(strs: list[str]) -> str:
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0

        while i < min_length:
            for s in strs:
              if s[i] != strs[0][i]:
                return s[:i]
            i += 1        

        return s[:i]

print(longestCommonPrefix(strs1))                                     
print(longestCommonPrefix(strs2))                                     
