nums1 = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]

def sortedSquare(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1
    result.reverse()
    return result

print(sortedSquare(nums1))
print(sortedSquare(nums2))