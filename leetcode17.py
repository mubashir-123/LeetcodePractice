class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Time O(n * 4 ** n) Space O(n)
        if digits == '':
            return []
        
        M = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6':'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        n = len(digits)
        res, sol = [], []

        def backTrack(i = 0):
            if n == i:
                res.append(''.join(sol))
                return
            
            for letter in M[digits[i]]:
                sol.append(letter)
                backTrack(i + 1)
                sol.pop()

        backTrack(0)
        return res


digits1 = "23"
digits2 = ""
digits3 = "2"
digits4 = "74"

sol = Solution()
print("Digits 1: ",sol.letterCombinations(digits1))
print("Digits 2: ",sol.letterCombinations(digits2))
print("Digits 3: ",sol.letterCombinations(digits3))
print("Digits 4: ",sol.letterCombinations(digits4))