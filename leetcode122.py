
def maxProfit(prices: list[int]) -> int:
    # Time O(n)
    # Space O(1)
    profit = 0
    n = len(prices)

    for i in range(1,n):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

prices1 = [7,1,5,3,6,4]
print(maxProfit(prices1))

prices2 = [1,2,3,4,5]
print(maxProfit(prices2))

prices3 = [7,6,4,3,1]
print(maxProfit(prices3))