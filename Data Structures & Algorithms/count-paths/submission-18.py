class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # time = O(m*n)
        # space = O(m*n)
        dp = [[0 for j in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = 1

        # bottom up dp
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # sum of bottom and right
                dp[i][j] += dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
        