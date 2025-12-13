
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

# Time: O(n) Space: O(1)
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

print(maxProfit(prices1))            
print(maxProfit(prices2))            

