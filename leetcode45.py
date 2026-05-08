def jump(nums: list[int]) -> int:
    # Time O(n)
    # Space O(1)
    smallest = 0
    n = len(nums)
    far, end = 0, 0

    for i in range(n-1):
        far = max(far,i + nums[i])

        if i == end:
            smallest += 1
            end = far
    
    return smallest

nums1 = [2,3,1,1,4]
print(jump(nums1))

nums2 = [2,3,0,1,4]
print(jump(nums2))