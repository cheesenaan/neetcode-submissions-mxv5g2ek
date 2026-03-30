class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # dp[x] = distinct comb of coins equal x
        dp = [0] * (amount+1)
        dp[0] = 1 # 1 way to make 0

        # reverse order will give permutation - this one gives comb
        for c in coins:
            for x in range(c, amount+1): 
                dp[x] += dp[x-c]

        return dp[amount]       