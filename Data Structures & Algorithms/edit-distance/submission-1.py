class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)
        dp = [[float("inf") for j in range(n+1)] for i in range(m+1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i


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