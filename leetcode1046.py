import heapq

class Solution:
     def lastStoneWeight(self, stones: list[int]) -> int:
        # Time O(n logn) Space O(1)
        stones = stones[:] # To make a copy of list as heap destroys the original list 
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones,largest - next_largest)
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

stones1 = [2,7,4,1,8,1]
stones2 = [1]

sol = Solution()
result1 = sol.lastStoneWeight(stones1)
print("Stones 1: ",stones1)
print("Last weight of stone 1: ",result1)

result2 = sol.lastStoneWeight(stones2)
print("Stones 1: ",stones2)
print("Last weight of stone 1: ",result2)