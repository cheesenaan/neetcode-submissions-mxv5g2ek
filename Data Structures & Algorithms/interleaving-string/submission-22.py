class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i,j) in dp:
                return dp[(i,j)]

            res = False
            if i < len(s1) and s1[i] == s3[i+j]:
                res = dfs(i+1,j)
            
            if j < len(s2) and s2[j]  == s3[i+j]:
                res = dfs(i,j+1)

            dp[(i,j)] = res
            return dp[(i,j)]

        # return dfs(0,0)

        dp = [[False for j in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i+1][j]
                if j < len(s2) and s2[j]  == s3[i+j]:
                    dp[i][j] =  dp[i][j+1]

        return dp[0][0]
