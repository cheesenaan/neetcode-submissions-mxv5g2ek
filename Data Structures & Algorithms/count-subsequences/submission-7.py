class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # memo = {}
        # def dfs(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     res = 0
        #     if s[i] == t[j]:
        #         res += dfs(i+1, j+1)
        #         res += dfs(i+1, j)
        #     else:
        #         res += dfs(i+1, j)

        #     memo[(i,j)] = res
        #     return res

        # return dfs(0,0)

        m, n = len(s), len(t)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m + 1):
            dp[i][n] = 1


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
                    dp[i][j] += dp[i+1][j]
                else:
                    dp[i][j] += dp[i+1][j]

        return dp[0][0]
