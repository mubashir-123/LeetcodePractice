nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]

# Time O(lon(n))
# Space O(1)

def findMin(nums: list[int]) -> int:
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        m = (r + l) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]

print(findMin(nums1)) 
print(findMin(nums2)) 