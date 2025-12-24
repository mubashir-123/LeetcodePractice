nums1 = [1,3,5,6]
target1 = 5
nums2 = [1,3,5,6]
target2 = 2
nums3 = [1,3,5,6]
target3 = 7

def searchInsert(nums: list[int], target: int) -> int:
        # n = len(nums)
        # l = 0
        # r = n - 1

        # while l <= r:
        #     m = (l + r) // 2

        #     if nums[m] == target:
        #         return m 
            
        #     elif nums[m] < target:
        #         l = m + 1
            
        #     else:
        #         r = m - 1
        # return l

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                        return m
                elif nums[m] < target:
                        l = m + 1
                else:
                        r = m - 1
        return l
print(searchInsert(nums1,target1))
print(searchInsert(nums2,target2))
print(searchInsert(nums3,target3))