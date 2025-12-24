class Solution:
    # Time O(N choose k) Space O(N)
    def combine(self,n: int,k :int) -> list[list[int]]:
        ans, sol = [], []

        def backTrack(x):
            if len(sol) == k:
                ans.append(sol[:])
                return

            left = x
            still_need = k - len(sol)

            if left > still_need:
                backTrack(x - 1)

            sol.append(x)
            backTrack(x - 1)
            sol.pop()
        
        backTrack(n)
        return ans

n1 = 4
k1 = 2
n2 = 1
k2 = 1 

sol = Solution()
print("Combiantion 1: ",sol.combine(n1,k1))
print("Combiantion 2: ",sol.combine(n2,k2))