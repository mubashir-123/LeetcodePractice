nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

def productExceptSelf(nums: list[int]) -> list[int]:
    # Time O(n) Space O(n) left and right array approach
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n

    for i in range(n):
        j = -i - 1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]

    return [l * r for l,r in zip(l_arr,r_arr)] # Multiply left and right array for final result

print(productExceptSelf(nums1))
print(productExceptSelf(nums2))
