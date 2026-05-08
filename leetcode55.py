def canJump(nums: list[int]) -> bool:
    # Greedy appraoch starts from end
    # Time O(n)
    # Space O(1)
    n = len(nums)
    target = n - 1

    for i in range(n-1, -1, -1):
        max_jump = nums[i]
        if i + max_jump >= target:
            target = i
    
    return target == 0

nums1 = [2,3,1,1,4]
print(canJump(nums1))

nums2 = [3,2,1,0,4]
print(canJump(nums2))
