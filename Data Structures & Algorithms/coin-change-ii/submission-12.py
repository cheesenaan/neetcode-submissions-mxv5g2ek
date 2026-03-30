class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # time = O(n*a) where n is number of counts and a = amount
        # space = O(a)
        
        # dp[x] = number of DISTINCT combinations to make amount x
        # (Contrast with Coin Change I:
        #  dp[x] = minimum number of coins to make amount x)
        dp = [0] * (amount + 1)

        # Base case:
        # There is exactly ONE way to make amount 0:
        # choose no coins at all
        #
        # (Contrast with Coin Change I:
        #  dp[0] = 0 because 0 coins are needed to make 0)
        dp[0] = 1

        # IMPORTANT LOOP ORDER:
        # We iterate over coins FIRST to ensure combinations are counted
        # and permutations are NOT double-counted.
        #
        # If we reversed the loops (amount outer, coins inner),
        # then [1,2] and [2,1] would be counted as different ways ❌
        for c in coins:

            # For each coin, update all reachable amounts
            # We start from c because amounts smaller than c
            # cannot include this coin
            for x in range(c, amount + 1):

                # Transition:
                # If we use coin c as part of a combination for amount x,
                # then the remaining amount is (x - c).
                #
                # The number of ways to make x USING coin c
                # is exactly the number of ways to make (x - c)
                #
                # We ADD because we are COUNTING combinations,
                # not minimizing anything
                #
                # (Contrast with Coin Change I:
                #  dp[x] = min(dp[x], dp[x - c] + 1))
                dp[x] += dp[x - c]

        # Final answer:
        # Number of distinct combinations to make `amount`
        return dp[amount]
