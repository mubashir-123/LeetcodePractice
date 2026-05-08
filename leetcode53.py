def maxSubArray(nums: list[int]) -> int:
    curr_sum = 0
    max_sum = float('-inf')

    for i in range(len(nums)):
        curr_sum += nums[i]
        max_sum = max(max_sum,curr_sum)

        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums1))

nums2 = [1]
print(maxSubArray(nums2))

nums3 = [5,4,-1,7,8]
print(maxSubArray(nums3))