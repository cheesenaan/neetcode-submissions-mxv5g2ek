class Solution:
    def climbStairs(self, n: int) -> int:

        # brute force is o(2^n)

        # bottom up dp o(n) time and space
        
        # if n <= 2:
        #     return n

        # dp = [0] * (n+1)
        # dp[0], dp[1], dp[2] = 1, 1, 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        # optimal
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one




        
        