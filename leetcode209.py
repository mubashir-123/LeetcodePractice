target1 = 7
nums1 = [2,3,1,2,4,3]
target2 = 4
nums2 = [1,4,4]
target3 = 11
nums3 = [1,1,1,1,1,1,1,1]

def minSubArrayLen(target: int, nums: list[int]) -> int:
    # Time O(n) Space O(1)
    min_count = float('inf')
    l = 0
    summ = 0

    for r in range(len(nums)):
        summ += nums[r]
        while summ >= target:
            min_count = min(min_count, (r - l + 1))
            summ -= nums[l]
            l += 1
    return min_count if min_count < float('inf') else 0

print(minSubArrayLen(target1,nums1))
print(minSubArrayLen(target2,nums2))
print(minSubArrayLen(target3,nums3))
