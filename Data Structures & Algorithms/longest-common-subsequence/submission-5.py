class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # dp[j] = LCS length for text1[i:] and text2[j:]
        dp = [0] * (n + 1)

        # iterate text1 backwards
        for i in range(m - 1, -1, -1):
            prev_diag = 0  # represents dp[i+1][j+1]
            for j in range(n - 1, -1, -1):
                temp = dp[j]  # save dp[i+1][j] before overwriting
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev_diag = temp

        return dp[0]
