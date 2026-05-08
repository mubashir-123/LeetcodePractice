def lengthOfLIS(nums: list[int]) -> int:
    # Using Binary search appraoch
    # Time O(n logn)
    #  Space O(n)
    
    temp = []

    def binary_search(temp,num):
        lo, hi = 0, len(temp) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if temp[mid] == num:
                return mid
            elif temp[mid] < num:
                 lo = mid + 1
            else:
                hi = mid - 1
        return lo

    for num in nums:
        i = binary_search(temp,num)
        if i < len(temp):
            temp[i] = num
        else:
            temp.append(num)
    return len(temp)

nums1 = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums1))

nums2 = [0,1,0,3,2,3]
print(lengthOfLIS(nums2))

nums3 = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums3))