class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m ,n = len(text1), len(text2)

        dp = [0] * (n+1)

        for i in range(m - 1, -1, -1):
            diag = 0
            for j in range(n-1, -1, -1):
                temp = dp[j] # store dp[i+1][j]
                if text1[i] == text2[j]:
                    # diagonal
                    dp[j] = 1 + diag
                else:
                    # max of bottom or right
                    dp[j] = max(dp[j], dp[j + 1])
                diag = temp

        return dp[0]