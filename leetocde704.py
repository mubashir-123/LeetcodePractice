nums1 = [-1,0,3,5,9,12]
target1 = 9

nums2 = [-1,0,3,5,9,12]
target2 = 2

# Time O(logn)
# Space O(1)

def search(nums:list[int],target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (right+left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(search(nums1,target1))
print(search(nums2,target2))