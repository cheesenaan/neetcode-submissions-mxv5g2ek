class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # bottom up dp. sum bottom and right
        # time : O(n^2)
        # space : O(n^2)
        # dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # dp[m-1][n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         dp[i][j] += dp[i+1][j] + dp[i][j+1]

        # return dp[0][0]

        # bottom up dp. sum bottom and right
        # use only one array
        # time : O(m*n)
        # space : O(n)
        # dp = [1] * (n)
        # for i in range(m-1):
        #     for j in range(n-2, -1, -1):
        #         dp[j] += dp[j+1]

        # return dp[0]

        # math
        # m-1 moves down, and n-1 moves right = m+n-2
        # this is permuation 
        return math.comb(m+n-2, m-1)




        