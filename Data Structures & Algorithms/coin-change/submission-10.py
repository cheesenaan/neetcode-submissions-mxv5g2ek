class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[x] = min coins at amount x 
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for x in range(amount+1):
            for c in coins:
                if x >= c:
                    dp[x] = min(dp[x], dp[x-c]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

        