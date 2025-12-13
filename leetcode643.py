nums1 = [1,12,-5,-6,50,3]
k1 = 4
nums2 = [5]
k2 = 1

def findMaxAverage(nums: list[int], k: int) -> float:
    # Time O(n) Space O(1)
    n = len(nums)
    summ = 0

    for i in range(k):
        summ += nums[i]
    max_avg = summ / k

    for i in range(k,n):
        summ += nums[i]
        summ -= nums[i - k]

        avg = summ / k
        max_avg = max(max_avg,avg)
    return max_avg

print(findMaxAverage(nums1,k1))
print(findMaxAverage(nums2,k2))

