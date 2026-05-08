
def sortColors(nums: list[int]) -> None:
    # Time O(n)
    # Space O(1)
    # Dutch National Flag (DNF) Algorithm
    lo = 0
    mid = 0
    hi = len(nums) - 1

    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
    return nums

nums1 = [2,0,2,1,1,0]
print(sortColors(nums1))

nums2 = [2,0,1]
print(sortColors(nums2))