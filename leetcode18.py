def fourSum(nums: list[int], target: int) -> list[list[int]]:
    # Time O(n^3)
    # Space(n)
    n = len(nums)
    answer = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1,n):
            if j < i + 1 and nums[j] == nums[j - 1]:
                continue
            lo,hi = j + 1,n - 1
            while lo < hi:
                summ = nums[i] + nums[j] + nums[lo] + nums[hi]
                if summ == target:
                    answer.append([nums[i] , nums[j] , nums[lo] , nums[hi]])
                    lo += 1
                    hi -= 1
                    
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi  and nums[hi] == nums[hi - 1]:
                        hi -= 1
                elif summ < target:
                    lo += 1
                else:
                    hi -= 1
    return answer

nums1 = [1,0,-1,0,-2,2]
target1 = 0
print(fourSum(nums1,target1))

nums2 = [2,2,2,2,2]
target2 = 8
print(fourSum(nums2,target2))