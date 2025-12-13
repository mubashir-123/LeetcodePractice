nums1 = [0,1,2,4,5,7]
nums2 = [0,2,3,4,6,8,9]

def summaryRanges(nums: list[int]) -> list[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) -1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if start != nums[i]:
                ans.append(str(start)+ "->"+str(nums[i]))
            else:
                ans.append(str(nums[i]))
            i += 1

        return ans

print(summaryRanges(nums1))
print(summaryRanges(nums2))

# Time O(n) Space O(n)