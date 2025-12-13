nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3

def longestOnes(nums: list[int],k: int) -> int:
    # Time O(n) Space O(1)
    max_w = 0
    num_zeros = 0
    n = len(nums)
    r = n - 1
    l = 0

    for r in range(n):
        if nums[r] == 0:
            num_zeros += 1
        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1
        w = r - l + 1
        max_w = max(max_w,w)
    return max_w

print(longestOnes(nums1,k1))
print(longestOnes(nums2,k2))