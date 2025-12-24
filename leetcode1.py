nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

def twoSum(nums: list[int], target: list[int]):
    h = {}

    for i in range(len(nums)):
        h[nums[i]] = i

    for i in range(len(nums)):
        y = target - nums[i]

        if y in h and h[y] != i:
           return [i,h[y]]
        
print(twoSum(nums1,target1))

