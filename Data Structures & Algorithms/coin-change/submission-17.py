class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for x in range(amount + 1):
            for c in coins:
                if x >= c:
                    dp[x] = min(dp[x], dp[x-c]+1)

        return dp[-1] if dp[-1] != float('inf') else -1
        