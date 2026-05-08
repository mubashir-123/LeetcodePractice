
def minCostClimbingStairs(cost: list[int]) -> int:
    # Bottom Up (Contant space)
    # Time O(n) Space O(1)
    n = len(cost)
    prev, curr = 0, 0

    for i in range(2, n + 1):
        prev, curr = curr, min(cost[i - 2] + prev, cost[i - 1]+ curr)
    
    return curr

cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]

print(minCostClimbingStairs(cost1))
print(minCostClimbingStairs(cost2))