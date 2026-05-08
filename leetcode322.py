
def coinChange(coins: list[int], amount: int) -> int:
    # Bottom Up DP [Tabulation]
    # Time O(Coins * Amount)
    # Space O(Amount)
    
    coins.sort()
    dp = [0] * (amount + 1)

    for i in range(1,amount + 1):
        minn = float('inf')
        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            minn = min(minn, (dp[diff] + 1))
        dp[i] = minn
    
    if dp[amount] < float('inf'):
        return dp[amount]
    else:
        return -1

coins1 = [1,2,5]
amount1 = 11
print(coinChange(coins1,amount1))

coins2 = [2]
amount2 = 3
print(coinChange(coins2,amount2))

coins3 = [1]
amount3 = 0
print(coinChange(coins3,amount3))

coins4 = [474,83,404,3]
amount4 = 264
print(coinChange(coins4,amount4))