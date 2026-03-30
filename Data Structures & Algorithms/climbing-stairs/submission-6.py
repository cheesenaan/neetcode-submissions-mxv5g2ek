class Solution:
    def climbStairs(self, n: int) -> int:

        
        # brute force is o(2^n)



        # instead of recalucating, cache and re use answer o(n) time and space
        if n == 1 or n == 2:
            return n
        
        # bottom up
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]


        return dp[n]
        
        # o(n) time and o(1) space
       
        # last two in Fibonacci always 1
        # one, two = 1, 1

        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp

        # return one