nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

def containDuplicate(nums: list[int]) -> bool:
    h = set()

    for n in nums:
        if n in h:
            return True
        else:
            h.add(n)
    return False

print(containDuplicate(nums1))
print(containDuplicate(nums2))
print(containDuplicate(nums3))
