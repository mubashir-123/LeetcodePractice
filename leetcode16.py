
def threeSumClosest(nums: list[int], target: int) -> int:
    # Time O(n^2)
    # Space O(n)

    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            curr_sum = nums[i] + nums[lo] + nums[hi]
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
            elif curr_sum == target:
                return curr_sum
            elif curr_sum < target:
                lo += 1
            else:
                hi -= 1
    return closest_sum

nums1 = [-1,2,1,-4]
target1 = 1
print(threeSumClosest(nums1,target1))

nums2 = [0,0,0]
target2 = 1
print(threeSumClosest(nums2,target2))