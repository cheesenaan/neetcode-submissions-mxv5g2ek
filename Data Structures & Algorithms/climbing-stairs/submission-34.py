class Solution:
    def climbStairs(self, n: int) -> int:

        # dp[i] = number of ways to reach top from i
        
        # backwards 
        # dp = [0] * (n+1)
        # dp[0], dp[1] = 1, 1
        one, two = 1, 1

        for i in range(2, n+1):
            temp = one
            one = one + two
            two = temp

        return one


        