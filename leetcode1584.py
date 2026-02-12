import heapq
def minCostConnectPoints(points: list[list[int]]) -> int:
    # prim's Algorithm
    n = len(points)
    total_cost = 0
    min_heap = [(0,0)]
    seen = set()

    while len(seen) < n:
        dist, i = heapq.heappop(min_heap)
        if i in seen:
            continue
        seen.add(i)
        total_cost += dist
        xi, yi = points[i]

        for j in range(n):
            if j not in seen:
                xj, yj = points[j]
                nei_dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(min_heap, (nei_dist,j))
    
    return total_cost

points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points2 = [[3,12],[-2,5],[-4,1]]

print("Total cost1: ",minCostConnectPoints(points1))
print("Total cost2: ",minCostConnectPoints(points2))

# Time O(n^2 log(n)) or O(E log(E))
# Space O(n^2) or O(E)
