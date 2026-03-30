class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x] will store the minimum number of coins needed to make amount x
        # Initialize all values to infinity (meaning not yet reachable)
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Iterate through all amounts from 1 to target amount
        for x in range(1, amount + 1):
            # Try using each coin denomination
            for c in coins:
                # Only consider the coin if it does not exceed the current amount
                if x >= c:
                    # Update dp[x] by choosing the minimum between:
                    # 1) its current value
                    # 2) using one coin c plus the best way to make (x - c)
                    dp[x] = min(dp[x], dp[x - c] + 1)

        # If dp[amount] is still infinity, it means the amount cannot be formed
        # Otherwise, return the minimum number of coins needed
        return dp[amount] if dp[amount] != float('inf') else -1
