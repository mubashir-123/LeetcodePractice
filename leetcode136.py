
def singleNumber(nums: list[int]) -> int:
   # Time O(n) Space O(1)
    a = 0

    for x in nums:
        a ^= x
    return a

nums1 = [2,2,1]
print(singleNumber(nums1))

nums2 = [4,1,2,1,2]
print(singleNumber(nums2))

nums3 = [1]
print(singleNumber(nums3))