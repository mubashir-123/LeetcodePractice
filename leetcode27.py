def removeElement(nums: list[int], val: int) -> int:
    # Using two pointers approach
    # Time O(n)
    # Space O(1)
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n

nums1 = [3,2,2,3]
val1 = 3
print(removeElement(nums1,val1))

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(removeElement(nums2,val2))