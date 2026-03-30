class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        dp = [[float('inf') for j in range(len(word1)+1)] for _ in range(len(word2)+1)]

        # set last column to N, ... 5,4,3,2,1,0
        for i in range(len(word2)+1):
            dp[i][-1] = len(word2) - i

         # set last row to M, ... 5,4,3,2,1,0
        for i in range(len(word1)+1):
            dp[-1][i] = len(word1) - i

        
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i+1][j+1]
                    replace = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    dp[i][j] = min(insert, replace, delete)

        return dp[0][0]
