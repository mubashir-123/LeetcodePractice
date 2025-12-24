class Solution:
    def combinationSum(self,candidates: list[list[int]],target: int) -> list[list[int]]:
        # Time O(n ** t) Space O(n)
        res, sol = [], []
        nums = candidates
        nums.sort()
        n = len(nums)

        def backTrack(i,curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            for j in range(i,n):
                if curr_sum + nums[j] > target:
                    break

                sol.append(nums[j])
                backTrack(j,curr_sum + nums[j])
                sol.pop()
        
        backTrack(0,0)
        return res


candidates1 = [2,3,6,7]
target1 = 7

candidates2 = [2,3,5]
target2 = 8

candidates3 = [2]
target3 = 1

sol = Solution()
print("Combination Sum 1: ",sol.combinationSum(candidates1,target1))
print("Combination Sum 2: ",sol.combinationSum(candidates2,target2))
print("Combination Sum 3: ",sol.combinationSum(candidates3,target3))