nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]

def majorityElement(nums: list[int]) -> int:
    count = 0
    ans = -1

    for num in nums:
        if count == 0:
            ans = num

        if ans == count:
            count += 1
        else:
            count -= 1
    return ans

print(majorityElement(nums1))    
print(majorityElement(nums2))    
