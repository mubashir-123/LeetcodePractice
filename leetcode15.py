nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]

# Time O(n^2)
# Space O(n)

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            sums = nums[lo] + nums[i] + nums[hi]
            if sums == 0:
                answer.append([nums[lo], nums[i], nums[hi]])
                lo , hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif sums < 0:
                lo += 1
            else:
                hi =- 1
    return answer

print(threeSum(nums1))        
print(threeSum(nums2))        
print(threeSum(nums3))        
