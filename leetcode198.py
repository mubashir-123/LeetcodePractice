
def rob(nums: list[int]) -> int:
    # Botton Up DP (Constant Space)
    # Time O(n) Space O(1)

    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums(1))
    
    prev, curr = nums[0], max(nums[0],nums[1])

    for i in range(2,n):
        prev, curr = curr, max(nums[i] + prev, curr)
    
    return curr

nums1 = [1,2,3,1]
print(rob(nums1))

nums2 = [2,7,9,3,1]
print(rob(nums2))