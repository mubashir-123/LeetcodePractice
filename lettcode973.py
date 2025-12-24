import heapq
class Solution:
    def kCloset(self,points: list[list[int]],k :int) -> list[list[int]]:
        # Time O(n logk) Space O(k)
        def dist(x,y):
            return x ** 2 + y ** 2

        heap = []
        for x,y in points:
            d = dist(x,y)
            if len(heap) < k:
                heapq.heappush(heap,(-d,x,y))
            else:
                heapq.heappushpop(heap,(-d,x,y))
        return [(x,y) for d,x,y in heap]

points1 = [[1,3],[-2,2]]
k1 = 1

points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2

sol = Solution()
print("Points 1",points1)
result1 = sol.kCloset(points1,k1)
print("Closest point 1: ",result1)
print()
print("Points 2",points2)
result2 = sol.kCloset(points2,k2)
print("Closest point 2: ",result2)