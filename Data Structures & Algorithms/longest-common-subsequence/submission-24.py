class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # time - space O(m*n)
        # m,n = len(text1), len(text2)
        # dp = [[0 for j in range(n+1)] for _ in range(m+1)]
        # dp[m-1][n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # return dp[0][0]

        m,n = len(text1), len(text2)
        dp = [0] * (n+1)
        for i in range(m-1, -1, -1):
            diag = 0
            for j in range(n-1, -1, -1):
                temp = dp[j] # store bottom dp[i+1][j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + diag
                else:
                    dp[j] = max(dp[j], dp[j+1])
                diag = temp
        return dp[0]

