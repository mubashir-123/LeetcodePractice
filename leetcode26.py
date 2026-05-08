
def removeDuplicates(nums: list[int]) -> int:
    # Using 2 pointers appraoch
    # Time O(n)
    # Space O(1)
    n = len(nums)
    j = 1

    for i in range(1,n):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

nums1 = [1,1,2]
print(removeDuplicates(nums1))

nums2 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums2))