import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> list[int]:
       # Time O(n logk) space O(k)
        heap_num = []
        for num in nums:
            if len(heap_num) < k:
               heapq.heappush(heap_num,num)
            else:
               heapq.heappushpop(heap_num,num)
        return heap_num[0]

nums1 = [3,2,1,5,6,4]
k1 = 2
nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4

sol = Solution()
print("Input nums 1: ",nums1)
result1 = sol.findKthLargest(nums1,k1)
print("Largest kth element 1: ",result1)

print("Input nums 2: ",nums2)
result2 = sol.findKthLargest(nums2,k2)
print("Largest kth element 1: ",result2)