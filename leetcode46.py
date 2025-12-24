class Solution:
    # Time O(n!) Space O(n)
    def permute(self,nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans

nums1 = [1,2,3]
nums2 = [0,1]
nums3 = [1]

sol = Solution()
result1 = sol.permute(nums1)
print("Permute 1: ",result1)

result2 = sol.permute(nums2)
print("Permute 2: ",result2)

result3 = sol.permute(nums3)
print("Permute 3: ",result3)