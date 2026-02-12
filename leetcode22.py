n1 = 3
n2 = 1

def generateParenthesis(n: int) -> list[str]:
    # Time O(2 ** n) Space O(n)
    # ans, sol = [], []

    # def backTrack(openn,close):
    #     if len(sol) == 2*n:
    #         ans.append(''.join(sol))
    #         return
        
    #     if openn < n:
    #         sol.append('(')
    #         backTrack(openn + 1,close)
    #         sol.pop()
        
    #     if openn > close:
    #         sol.append(')')
    #         backTrack(openn, close + 1)
    #         sol.pop()
        
    # backTrack(0,0)
    # return ans

    ans,sol = [], []
    def backTrack(open,close):
        if len(sol) == 2*n:
            ans.append(''.join(sol))
            return
        
        if open < n:
            sol.append('(')
            backTrack(open + 1,close)
            sol.pop()
        
        if open > close:
            sol.append(')')
            backTrack(open,close + 1)
            sol.pop()
    backTrack(0,0)
    return ans

print(generateParenthesis(n1))
print(generateParenthesis(n2))