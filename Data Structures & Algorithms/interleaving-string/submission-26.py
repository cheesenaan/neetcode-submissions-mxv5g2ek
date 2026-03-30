class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # if len(s1) + len(s2) != len(s3):
        #     return False

        # memo = {}
        # def dfs(i, j):
        #     if i == len(s1) and j == len(s2):
        #         return True

        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     res = False
        #     if i < len(s1) and s1[i] == s3[i+j]:
        #         res = dfs(i+1, j)

        #     if j < len(s2) and s2[j] == s3[i+j]:
        #         res = dfs(i, j+1)

        #     memo[(i,j)] = res
        #     return res

        # return dfs(0,0)

        if len(s1) + len(s2) != len(s3):
            return False
        
        m , n = len(s1), len(s2)
        dp = [[False for j in range(n+1)] for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < len(s1) and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i+1][j]

                if j < len(s2) and s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j+1]

        return dp[0][0]



        