class Solution:
    def climbStairs(self, n: int) -> int:

        # dp[i] = number of steps from ith floor
        dp = [0] * (n+1)
        # reversed or backwards
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


       



       