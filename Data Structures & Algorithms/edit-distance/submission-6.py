class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)
        dp = [[float("inf") for j in range(n+1)] for i in range(m+1)]

        for col in range(n+1):
            dp[m][col] = n - col

        for row in range(m+1):
            dp[row][n] = m - row

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]  
                    dp[i][j] = min(insert, delete, replace)  
        return dp[0][0]