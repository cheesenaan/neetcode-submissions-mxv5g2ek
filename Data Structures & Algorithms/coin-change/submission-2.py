class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        # find number of coins needed to total x amount
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for x in range(1, amount+1):
            for c in coins:
                if x >= c:
                    dp[x] = min(dp[x], dp[x-c]+1)

        return dp[amount] if dp[amount] != float('inf') else -1



        # # Memoization dictionary
        # # Key   -> (current total, current index in coins)
        # # Value -> number of ways to form 'amount' from this state
        # memo = {}

        # # dfs(total, i) returns the number of ways to form 'amount'
        # # using coins[i:] starting from the current total
        # def dfs(total, i):
        #     # BASE CASE 1:
        #     # If we have exactly reached the target amount,
        #     # count this as 1 valid combination
        #     if total == amount:
        #         return 1

        #     # BASE CASE 2:
        #     # If we have exceeded amount or used all coins,
        #     # no valid combination can be formed
        #     if total > amount or i >= len(coins):
        #         return 0

        #     # MEMOIZATION CHECK:
        #     # If we already solved this subproblem, return cached result
        #     if (total, i) in memo:
        #         return memo[(total, i)]

        #     # OPTION 1: take the current coin (can use unlimited times)
        #     take = dfs(total + coins[i], i)

        #     # OPTION 2: skip the current coin and move to the next coin
        #     skip = dfs(total, i + 1)

        #     # Store the total number of combinations for this state
        #     memo[(total, i)] = take + skip

        #     return memo[(total, i)]

        # # Start recursion from total = 0 and first coin index = 0
        # return dfs(0, 0)


