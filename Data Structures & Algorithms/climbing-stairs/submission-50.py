class Solution:
    def climbStairs(self, n: int) -> int:

        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 1, 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        prev2, prev1 = 1, 1
        for i in range(2, n + 1):
            tmp = prev2 + prev1
            prev2 = prev1
            prev1 = tmp
        return prev1

